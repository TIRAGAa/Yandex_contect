"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/53688/problems/
"""


# A. Барометр Фибоначчи
version_list = {0: 1, 1: 1}


def barometer(V):
    if V in version_list:
        return version_list[V]
    version_list[V] = barometer(V-1) + barometer(V-2)
    return version_list[V]


def main():
    version = int(input())
    result = barometer(version)
    print(result)


if __name__ == '__main__':
    main()


# B. Проект С.Ч.И.Т.А.Л.К.А.
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
