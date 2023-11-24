"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/52718/problems/
"""


# A. Количество чисел, меньших, чем заданное
def numbers(nums):
    result = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)

    return result


def main():
    nums = list(map(int, input().split()))
    result = numbers(nums)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()


# B. Поиск подстроки
def substring(data):
    min_w = 0
    folder = {}
    end_sub = 0

    for i in range(len(data)):
        if data[i] in folder:
            min_w = max(folder[data[i]]+1, min_w)
        end_sub = max(end_sub, i-min_w+1)
        folder[data[i]] = i

    return end_sub


def main():
    data = input()
    result = substring(data)
    print(result)


if __name__ == '__main__':
    main()
