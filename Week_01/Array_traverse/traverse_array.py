def traverse_array(arr):
    print("Index | Element | Simulated Memory Offset")
    print("------------------------------------------")
    element_size_bytes = 4  
    base_address = 1000
    
    for i in range(len(arr)):
        simulated_address = base_address + (i * element_size_bytes)
        print(f"  {i}   |    {arr[i]}   | Address: {simulated_address}")

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    traverse_array(data)