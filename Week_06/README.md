学习笔记


冒泡排序

嵌套循环 每次查找相邻的元素 如果逆序 则交换

插入排序

从前到后逐步构建有序序列 对于未排序数据 在已经排序序列向前扫描 找到相应位置则插入

选择排序

每次找到最小值 放到待排序数组的起始位置


快排

数组取标杆 pivot
小的在左边 大的在右边

依次对左右的进行快排


归并排序



堆排序

数组元素依次建立小顶堆
依次取堆顶元素 并删除




简单题目

数组的相对排序（谷歌在半年内面试中考过）
有效的字母异位词（Facebook、亚马逊、谷歌在半年内面试中考过）
字符串中的第一个唯一字符
（亚马逊、微软、Facebook 在半年内面试中考过）
反转字符串 II （亚马逊在半年内面试中考过）
翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）
反转字符串中的单词 III （微软、字节跳动、华为在半年内面试中考过）
仅仅反转字母（字节跳动在半年内面试中考过）
同构字符串（谷歌、亚马逊、微软在半年内面试中考过）
验证回文字符串 Ⅱ（Facebook 在半年内面试中常考）

中等题目

LRU 缓存机制（亚马逊、字节跳动、Facebook、微软在半年内面试中常考）
合并区间（Facebook、字节跳动、亚马逊在半年内面试中常考）
最长上升子序列（字节跳动、亚马逊、微软在半年内面试中考过）
解码方法（字节跳动、亚马逊、Facebook 在半年内面试中考过）
字符串转换整数 (atoi) （亚马逊、微软、Facebook 在半年内面试中考过）
找到字符串中所有字母异位词（Facebook 在半年内面试中常考）
最长回文子串（亚马逊、字节跳动、华为在半年内面试中常考）


排序算法


1.非线性时间比较类排序  
1.1 交换排序： 冒泡排序；快速排序  
1.2 插入排序： 简单插入排序；希尔排序  
1.3 选择排序： 简单选择排序；堆排序  
1.4 归并排序： 二路归并排序 

2.线性时间非比较类排序  
2.1 基数排序；  
2.2 桶排序；  
2.3 计数排序  


```python

import time
from functools import wraps


def calculate_time(place=2):
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
def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(0, length - i - 1):  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
    
# 每次在无序区中选择最小的元素，与无序区的第一个元素交换位置，则有序区扩展一；以此类推，直至所有元素排序完毕。
# 有序区arr[:sorted]; 无序区arr[sorted:] (sorted为已排序部分最大index;初始为0)
# 在无序区中找到最小的元素，swap(arr[sorted], arr[minIndex])
# sorted += 1
# 重复1-3，直至所有元素排序完毕。
def selectionSort(arr):
    length = len(arr)
    for i in range(length - 1): # the first ind of the unsorted
        minIdx = i              # the minIdx of the unsorted
        for j in range(i+1, length):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr
    
    
# 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
# 有序区 arr[:sorted]; 无序区 arr[sorted:] (初始状态认为第0个元素为已排序的，sorted = 1)
# 取出无序区的第一个元素的值，temp = arr[sorted]
# 将该值从后向前依次与有序区元素arr[i]比较，若temp < arr[i]，则将arr[i]后移；否则，将temp的值插入在(i+1)位置处。
# 重复1-3直至整个数组排序完成。
def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):  # the current element index
        preIndex = i - 1        # the index to insert
        current = arr[i]        # save the number otherwise it will be replace by others
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
import math
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
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
  
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 
    return arr

```



