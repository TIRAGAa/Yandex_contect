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
