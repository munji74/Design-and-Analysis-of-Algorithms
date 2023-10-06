# Design-and-Analysis-of-Algorithms

Quick Sort
Quick Sort is a highly efficient and widely used divide-and-conquer sorting algorithm known for its average-case time complexity of O(n log n). Quick Sort works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, based on whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.
![quicksort](https://github.com/munji74/Design-and-Analysis-of-Algorithms/assets/108124055/534fcf87-193c-4682-be12-479359beb7d5)


Sample code
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
Analysis:
Average-case time complexity: O(n log n)
Worst-case time complexity: O(n^2)
Best-case time complexity: O(n log n)

Counting Sort
Counting Sort is a non-comparative, integer-based sorting algorithm with a time complexity of O(n + k), where n is the number of elements to be sorted, and k is the range of input values. It is highly efficient for sorting data with a limited range of values, such as integers within a specific range. Counting Sort works by counting the frequency of each element in the input array and using that information to construct the sorted output array. It is particularly efficient when sorting integers or data types within a limited range, as it avoids the comparison of elements. Counting Sort is not suitable for sorting data with a wide range of values, as it requires additional memory for the counting array.
![count](https://github.com/munji74/Design-and-Analysis-of-Algorithms/assets/108124055/105ddb07-e680-4e7b-85ac-814b7ad49612)


Sample code
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count_array = [0] * (max_val - min_val + 1)
        for num in arr:
        count_array[num - min_val] += 1
    sorted_array = []
    for i, count in enumerate(count_array):
        sorted_array.extend([i + min_val] * count)
        return sorted_array
Analysis
Time complexity: O(n + k), where n is the number of elements and k is the range of input values. Space complexity: O(n + k) for the counting array.


Heap Sort

Heap Sort is a comparison-based sorting algorithm known for its average and worst-case time complexity of O(n log n). It uses a binary heap data structure to sort elements.
![heap](https://github.com/munji74/Design-and-Analysis-of-Algorithms/assets/108124055/756ff7d6-5760-42f2-88a9-164d519ea6d1)


Sample cod def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) e
