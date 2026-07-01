def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1   


if __name__ == "__main__":
    sample_data = [5, 3, 8, 4, 2, 9, 1]
    search_key = 4
    
    print(f"Searching for {search_key} in list: {sample_data}")
    result_index = linear_search(sample_data, search_key)
    
    if result_index != -1:
        print(f"Element found successfully at index: {result_index}")
    else:
        print("Element not found in the array.")