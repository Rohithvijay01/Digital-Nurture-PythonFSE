def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
            
        elif arr[mid] > target:
            high = mid - 1
            
        else:
            low = mid + 1

    return -1  


if __name__ == "__main__":
    sorted_data = [11, 15, 17, 19, 20, 77, 80]
    search_key = 77
    
    print(f"Searching for {search_key} in sorted array: {sorted_data}")
    result_index = binary_search(sorted_data, search_key)
    
    if result_index != -1:
        print(f"Element found successfully at index: {result_index}")
    else:
        print("Element not found in the array.")