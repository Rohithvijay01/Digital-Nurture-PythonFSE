def MergeSort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr

    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    leftsorted = MergeSort(left_half)
    rightsorted = MergeSort(right_half)

    return Merge(leftsorted, rightsorted)


def Merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1  
        else:
            sorted_array.append(right[j])  
            j += 1  

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])  

    return sorted_array


if __name__ == "__main__":
    sample_data = [20, 80, 77, 11, 15, 17, 19]
    print("Before Sorting:", sample_data)
    print("After Sorted: ", MergeSort(sample_data))