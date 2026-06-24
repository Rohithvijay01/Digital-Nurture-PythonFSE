def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    initial_arr = [1, 2, 3, 4, 5, 6]
    print("Original:", initial_arr)
    reverse_array_in_place(initial_arr)
    print("Reversed:", initial_arr)