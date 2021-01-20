学习笔记



Pypy从表面意思上面来说的话，就是用Python实现的Python。
但是更准确的描述应该是RPython实现的Python。
RPython是Python的子集，为什么到现在CPython一直没有加入JIT功能，
就是因为它的变量的类型是运行时确定的，也正是因为这样，JIT很难做。


PyPy首先使用这个RPython来把Python变成C源码，再执行。



双端队列支持线程安全，在双端队列的任何一端执行添加和删除操作，它们的内存效率几乎相同（时间复杂度为O(1)）。

虽然list也支持类似的操作，但是它对定长列表的操作表现很不错，而当遇到pop(0)和insert(0, v)这样既改变了列表的长度又改变其元素位置的操作时，其时间复杂度就变为O(n)了。

在双端队列中最好不使用切片( 如果使用deque进行切片的话会抛出异常)和索引( 和列表一样的使用，虽然效果上是一样的，但是可能效率上还是列表的索引效率更高一些)，你可以用popleft和appendleft方法，双端队列对这些操作做了优化。在两端的索引访问时间复杂度为O(1)，但是访问中间元素的时间复杂度为O(n)，速度较慢，对于快速随机的访问，还是用列表代替。

列表用于随机访问和定长数据的操作，包括切片，而双端队列适用于在两端压入或弹出元素，索引的效率可能低于列表，同时也不支持切片。




```
#define BLOCKLEN 64

typedef struct BLOCK {
    struct BLOCK *leftlink;
    PyObject *data[BLOCKLEN];
    struct BLOCK *rightlink;
} block;

typedef struct {
    PyObject_VAR_HEAD
    block *leftblock;
    block *rightblock;
    Py_ssize_t leftindex;       /* 0 <= leftindex < BLOCKLEN */
    Py_ssize_t rightindex;      /* 0 <= rightindex < BLOCKLEN */
    size_t state;               /* incremented whenever the indices move */
    Py_ssize_t maxlen;          /* maxlen is -1 for unbounded deques */
    PyObject *weakreflist;
} dequeobject;
```




一个块的内存容量为：8 + 8 * 64 + 8 = 528(bytes)，平均到data数组中的每一个 成员，

内存使用量为：528/64 = 8.25。是不是大大的节省了内存空间？

dequeobject 我没搞懂的是里面的 state ，每次操作他都会 +1 但是却没有看到 具体用途。

对于deque，pop popleft append appendleft 操作都是 O(1) 的时间效率，

因为 只要一动一下指针就行了。而 insert 时间复杂度为 O(N)，


其底层实现在 _deque_rotate 函数中（_deque_rotate函数的具体实现方式是每次移动一个块， 直到移动完n个数据为止），


insert操作的实现方式是，先把 insert(index, object) index左边的数据rotate到右边，然后插入，

然后再把刚才的数据rotate回来。



```python
class Queue:
    '''Create a queue object with a given maximum size.

    If maxsize is <= 0, the queue size is infinite.
    '''

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)

        # mutex must be held whenever the queue is mutating.  All methods
        # that acquire mutex must release it before returning.  mutex
        # is shared between the three conditions, so acquiring and
        # releasing the conditions also acquires and releases mutex.
        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def task_done(self):
        '''Indicate that a formerly enqueued task is complete.

        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).

        Raises a ValueError if called more times than there were items
        placed in the queue.
        '''
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished

    def join(self):
        '''Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        '''
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()

    def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        with self.mutex:
            return self._qsize()

    def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() == 0
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can grow before the result of empty() or
        qsize() can be used.

        To create code that needs to wait for all queued tasks to be
        completed, the preferred technique is to use the join() method.
        '''
        with self.mutex:
            return not self._qsize()

    def full(self):
        '''Return True if the queue is full, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() >= n
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can shrink before the result of full() or
        qsize() can be used.
        '''
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put(self, item, block=True, timeout=None):
        '''Put an item into the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        '''
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)

    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)

    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()

    __class_getitem__ = classmethod(types.GenericAlias)

```



从这初始化函数能得到哪些信息呢？首先，队列是可以设置其容量大小的，并且具体的底层存放元素的它使用了 collections.deque() 双端列表的数据结构，这使得能很方便的做先进先出操作。这里还特地抽象为 _init 函数是为了方便其子类进行覆盖，允许子类使用其他结构来存放元素（比如优先队列使用了 list）。

然后就是线程锁 self.mutex ，对于底层数据结构 self.queue 的操作都要先获得这把锁；再往下是三个条件变量，这三个 Condition 都以 self.mutex 作为参数，也就是说它们共用一把锁；从这可以知道诸如 with self.mutex 与 with self.not_empty 等都是互斥的。

基于这些锁而做的一些简单的操作：




```python

class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)

```




位置 /lib/python3.9/queue.py


优先队列使用了 heapq 模块的结构，也就是最小堆的结构。优先队列更为常用，队列中项目的处理顺序需要基于这些项目的特征，






