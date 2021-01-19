学习笔记



Pypy从表面意思上面来说的话，就是用Python实现的Python。
但是更准确的描述应该是RPython实现的Python。
RPython是Python的子集，为什么到现在CPython一直没有加入JIT功能，
就是因为它的变量的类型是运行时确定的，也正是因为这样，JIT很难做。


PyPy首先使用这个RPython来把Python变成C源码，再执行。




