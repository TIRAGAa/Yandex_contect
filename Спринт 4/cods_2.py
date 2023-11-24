"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/52598/problems/
"""


# A. Удаление дубликатов
def main():
    length_m = int(input())
    element_count = list(map(int, input(). split()))
    result = []
    sorted_element = []
    underlining = []

    for element in element_count:
        if element not in sorted_element:
            sorted_element.append(element)
            result.append(element)
        else:
            underlining.append('_')
    result.extend(underlining)

    print(' ' .join(map(str, result)))


if __name__ == '__main__':
    main()


# B. Определение индекса для вставки
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
