import time
from functools import wraps


def calculate_time(place=6):
    '''计算函数运行时间装饰器

    :param place: 显示秒的位数，默认为2位
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            beg = time.time()
            f = func(*args, **kwargs)
            end = time.time()
            s = '{}()：{:.%sf} s' % place
            print(s.format(func.__name__, end - beg))
            return f

        return wrapper

    return decorator


# 从前向后遍历未排序序列，如果当前元素 > 后一个元素，则交换这两个元素
# 重复1，直到排序完成
# 注意：第i轮遍历后，数组的第i大的元素已移动到数组[-i]位，数组的倒数第i位至最后一位是已经排序好的最大的i个元素；那么下一轮遍历时，仅需遍历arr[:-i]中的元素即可。
@calculate_time()
def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 每次在无序区中选择最小的元素，与无序区的第一个元素交换位置，则有序区扩展一；以此类推，直至所有元素排序完毕。
# 有序区arr[:sorted]; 无序区arr[sorted:] (sorted为已排序部分最大index;初始为0)
# 在无序区中找到最小的元素，swap(arr[sorted], arr[minIndex])
# sorted += 1
# 重复1-3，直至所有元素排序完毕。
@calculate_time()
def selectionSort(arr):
    length = len(arr)
    for i in range(length - 1):  # the first ind of the unsorted
        minIdx = i  # the minIdx of the unsorted
        for j in range(i + 1, length):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


# 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
# 有序区 arr[:sorted]; 无序区 arr[sorted:] (初始状态认为第0个元素为已排序的，sorted = 1)
# 取出无序区的第一个元素的值，temp = arr[sorted]
# 将该值从后向前依次与有序区元素arr[i]比较，若temp < arr[i]，则将arr[i]后移；否则，将temp的值插入在(i+1)位置处。
# 重复1-3直至整个数组排序完成。
@calculate_time()
def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):  # the current element index
        preIndex = i - 1  # the index to insert
        current = arr[i]  # save the number otherwise it will be replace by others
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]  # move -->
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr


# 希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。该方法因D.L.Shell于1959年提出而得名，是第一个突破O(n2)的排序算法。
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
def shellSort(start, end, number):
    increment = end - start + 1
    while increment > 1:
        increment //= 3 + 1
        for i in range(start + increment, end + 1):
            if number[i - increment] > number[i]:
                temp = number[i]
                j = i - increment
                while j >= start and number[j] > temp:
                    number[j + increment] = number[j]
                    j -= increment
                number[j + increment] = temp
    return number


# 采用分治法 (Divide and Conquer) 的一个非常典型的应用。将已有序的子序列合并，
# 得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。
@calculate_time()
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    return merge(mergeSort(left_arr), mergeSort(right_arr))


def merge(left_arr, right_arr):
    result = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    if i == len(left_arr):
        result.extend(right_arr[j:])
    elif j == len(right_arr):
        result.extend(left_arr[i:])
    return result


# 快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，
# 其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。快速排序同样采用了分治的思想。
@calculate_time()
def quickSort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    left = 0
    right = len(arr) - 1
    base = arr[left]
    while left < right:
        while arr[right] > base and right > left:
            right -= 1
        if right > left:
            arr[left] = arr[right]
            left += 1
        while arr[left] < base and left < right:
            left += 1
        if right > left:
            arr[right] = arr[left]
            right -= 1
    if left == right:
        arr[left] = base
        result = quickSort(arr[:left]) + [arr[left]]
        if left < len(arr) - 1:
            result = result + quickSort(arr[left + 1:])
        return result


# 计数排序
@calculate_time()
def countSort(arr, Max):
    bucket = [0] * (Max + 1)
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    idx = 0
    for i in range(len(bucket)):
        while bucket[i] > 0:
            arr[idx] = i
            idx += 1
            bucket[i] -= 1
    return arr


# 桶排序
@calculate_time()
def bucketSort(arr, bucketSize):
    if not arr:
        return arr
    minValue = min(arr)
    maxValue = max(arr)
    bucketsCount = (maxValue - minValue) // bucketSize + 1
    buckets = [[]] * bucketsCount
    for i in range(len(arr)):
        ind = (arr[i] - minValue) // bucketSize
        buckets[ind] = buckets[ind] + [arr[i]]
    arr = []
    for i in range(len(buckets)):
        buckets[i] = insertSort(buckets[i])
        for j in range(len(buckets[i])):
            arr.append(buckets[i][j])
    return arr


def insertSort(bucket):
    for i in range(1, len(bucket)):
        temp = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > temp:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = temp
    return bucket


# 基数排序

@calculate_time()
def LSDRadixSort(arr):
    Max = max(arr)
    radix = 0
    while Max != 0:
        Max /= 10
        radix += 1
    for i in range(1, radix + 1):
        bucket = [[] for i in range(10)]
        mod = pow(10, i)
        for j in range(len(arr)):
            base = arr[j] % mod
            base = base // pow(10, i - 1)
            bucket[base].append(arr[j])
        arr = []
        for k in range(10):
            for ele in bucket[k]:
                arr.append(ele)
    return arr


# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，
# 并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


@calculate_time()
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(bubbleSort(arr=arr))
    print(insertionSort(arr=arr))
    print(selectionSort(arr=arr))
    print(quickSort(arr=arr))
    print(mergeSort(arr=arr))
    print(heapSort(arr=arr))
    # shellSort(number=arr)
    nums = [73, 22, 93, 43, 55, 14, 28, 65, 39, 81]
    print(countSort(arr=nums, Max=100))
    print(bucketSort(arr=nums, bucketSize=100))
    print(LSDRadixSort(arr=nums))
