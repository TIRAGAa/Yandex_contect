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
