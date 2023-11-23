def find_target_index(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    index = find_target_index(arr, target)
    print(index)
