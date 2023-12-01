"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/53730/problems/
"""


# A. Сортировка по шаблону
def insertion_sort_with_pattern(arr, pattern):
    pattern_index = {value: index for index, value in enumerate(pattern)}

    def sort_key(container):
        return pattern_index.get(container, float('inf'))

    for i in range(1, len(arr)):
        key = arr[i]
        x = i - 1
        while x >= 0 and sort_key(arr[x]) > sort_key(key):
            arr[x + 1] = arr[x]
            x -= 1
        arr[x + 1] = key
    # Добавим неучтенные элементы в конец отсортированного массива
    unsorted_elements = [elem for elem in arr if elem not in pattern]
    arr = [elem for elem in arr if elem in pattern] + sorted(unsorted_elements)

    return arr


# Чтение входных данных
n = int(input())
arr_to_sort = list(map(int, input().split()))

m = int(input())
if m == 0:
    # Если шаблон отстствует, просто сортируем
    # массива sorted_arr = sorted(arr_to_sort)
    sorted_arr = sorted(arr_to_sort)
else:
    template_order = list(map(int, input().split()))
    # Сортировка массива с использованием шаблона
    sorted_arr = insertion_sort_with_pattern(arr_to_sort, template_order)

# Вывод отсортированного массива
print(*sorted_arr)


# B. Сортировка слиянием блоков
def sorted_b(n, arr):
    sorted_arr = sorted(enumerate(arr), key=lambda x: x[1])
    sorted_b = 0
    current_block_size = 0 

    for i, (oruginal_index, value) in enumerate(sorted_arr):
        current_block_size = max(current_block_size, oruginal_index + 1)

        if i == current_block_size - 1:
            sorted_b += 1
            current_block_size = 0

    return sorted_b


n = int(input())
arr = list(map(int, input().split()))

result = sorted_b(n, arr)
print(result)