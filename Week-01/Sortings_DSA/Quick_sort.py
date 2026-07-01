import random

def partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[low], arr[rand_pivot] = arr[rand_pivot], arr[low]

    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[low], arr[j] = arr[j], arr[low]
    return j


def qs(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        qs(arr, low, p_index - 1)
        qs(arr, p_index + 1, high)


if __name__ == "__main__":
    sample_data = [20, 80, 77, 11, 15, 17, 19]
    print("Before Sorting:", sample_data)
    
    qs(sample_data, 0, len(sample_data) - 1)
    
    print("After Sorted:  ", sample_data)