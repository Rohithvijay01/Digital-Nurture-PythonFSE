
def Insertion_sort(arr):
    n = len(arr)

    for i in range(1 , n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > arr[i]:
            arr[j + 1] = arr[j]
            j -= 1


        arr[j + 1] = key

    return arr   

if __name__ == "__main__":
    sample_data = [20, 80, 77, 11, 15, 17, 19]
    print("Before Sorting:", sample_data)
    print("After Sorted: ", Insertion_sort(sample_data))