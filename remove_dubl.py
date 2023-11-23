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

    print(' ' .join(map(str, result)), length_m)


if __name__ == '__main__':
    main()
