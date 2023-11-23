def counting_rhyme(men, tact):
    if men == 1:
        return 1
    else:
        return (1 + (counting_rhyme(men-1, tact) + tact - 1) % men)


def main():
    men = int(input())
    tact = int(input())
    result = counting_rhyme(men, tact)
    print(result)


if __name__ == '__main__':
    main()
