def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    test_arrays = [
        [3, 6, 8, 10, 1, 2, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 9, 1, 5, 6],
        [],
        [1],
        [2, 1]
    ]
    
    for arr in test_arrays:
        sorted_arr = quicksort(arr.copy())
        print(f"原数组: {arr}")
        print(f"排序后: {sorted_arr}")
        print()
