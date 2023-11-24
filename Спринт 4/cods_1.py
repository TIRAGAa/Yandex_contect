"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/26365/problems/
"""


# A. А + В
def main():
    a = int(input())
    b = int(input())
    print(a + b)


if __name__ in '__main__':
    main()


# В. Застежка молнии
def main():
    elements_count = int(input())
    first_array = input().split()
    second_array = input().split()
    result = []
    for element in range(elements_count):
        result.extend([first_array[element], second_array[element]])
    print(' '.join(result))


if __name__ == '__main__':
    main()


# C. Скользящее среднее
from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    # Здесь реализация вашего решения
    t = sum(arr[:window_size])
    res = [t / window_size]
    for i in range(window_size, len(arr)):
        t += arr[i] - arr[i - window_size]
        res.append(t / window_size)
    return res


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))


# D. Две фишки
"""НЕ СДЕЛАННО"""

# Е. Две фишки-2
"""НЕ СДЕЛАННО"""
