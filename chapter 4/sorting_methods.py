# Bubble sort, time complex O(n^2)
def BubbleSort(in_nums):
    nums = in_nums[:]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


# Selection sort, time complex O(n^2)
def SelectionSort(in_nums):
    nums = in_nums[:]
    for fillslot in range(len(nums) - 1, 0, -1):
        positionMax = 0
        for location in range(1, fillslot + 1):
            if nums[location] > nums[positionMax]:
                positionMax = location
        nums[positionMax], nums[fillslot] = nums[fillslot], nums[positionMax]
    return nums


# Insertion Sort, time complex O(n^2)
def InsertionSort(in_nums, start=0, gap=1):
    nums = in_nums[:]
    for idx in range(start+gap, len(nums), gap):
        cur_value = nums[idx]
        position = idx
        while position >= gap and nums[position - gap] > cur_value:
            nums[position] = nums[position - gap]
            position -= gap
        nums[position] = cur_value
    return nums


# Shell Sort, O(n) ~ O(n^2)
def ShellSort(in_nums):
    nums = in_nums[:]
    sublistCount = len(nums)//2
    while sublistCount > 0:
        for startPostion in range(sublistCount):
            nums = InsertionSort(nums, startPostion, sublistCount)
        sublistCount //= 2
    return nums


# Merge Sort, O(nlogn)
def mergeSort(in_nums):
    def helper(nums):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]
            helper(L)
            helper(R)

            i, j, k = 0, 0, 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

    nums = in_nums[:]
    helper(nums)
    return nums


# Quick Sort, O(nlogn)
def QuickSort(in_nums):
    def helper(nums, in_left, in_right):
        if in_left >= in_right:
            return 0
        left, right = in_left, in_right
        pivot = nums[in_right]

        while left < right:
            while left < right and nums[left] <= pivot:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

            while left < right and nums[right] >= pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]



        helper(nums, in_left, left-1)
        helper(nums, left+1, in_right)

    nums = in_nums[:]
    helper(nums, 0, len(nums)-1)
    return nums


import random

sample = [random.randrange(0, 1000) for _ in range(20)]
# sample = [2,3,7,4,2]
print(sample)
print(BubbleSort(sample))
print(SelectionSort(sample))
print(InsertionSort(sample))
print(ShellSort(sample))
print(mergeSort(sample))
print(QuickSort(sample))
print(sample)
