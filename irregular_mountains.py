def valid_arry(arr):
    height = len(arr)
    if height < 3:
        return False
    i = 0
    while i+1 < height and arr[i] < arr[i+1]:
        i += 1
    if i == 0 or i == height-1:
        return False
    while i+1 < height and arr[i] > arr[i+1]:
        i += 1
    return i == height - 1


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    alt_data = valid_arry(arr)
    print(alt_data)
