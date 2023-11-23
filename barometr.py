version_list = [0, 1]


def barometer(V):
    if V in version_list:
        return version_list[V]
    version_list.append(barometer(V-1) + barometer(V-2))
    print(version_list)
    return version_list[V]


def main():
    version = int(input())
    result = barometer(version)
    print(result)


if __name__ == '__main__':
    main()
