def print_array(array, size):
    for idx in range(size):
        if idx == size - 1:
            print(array[idx])
        else:
            print(f"{array[idx]} ", end="")