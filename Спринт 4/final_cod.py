"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/52720/problems/
"""


# A. Служба доставки
def delivery_service(cargo_weights: list, limit: int) -> int:
    '''
    Вычислает сколько потребуется траспортных
    платформ для перевозки роботов
    '''
    left = 0
    right = len(cargo_weights) - 1
    platforms = 0

    while left <= right:
        if cargo_weights[left] + cargo_weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1
    return platforms


def inputs():
    '''
    Запрашивает данные.
    Возврошяет кортетдж где:
    1 элемент это "Вес груза"
    2 элемент это "Лимит грузоподъёмности"
    '''
    cargo_weights = sorted(list(map(int, input().strip().split())))
    limit = int(input().strip())
    return cargo_weights, limit


def main():
    info = inputs()
    result = delivery_service(info[0], info[1])
    print(result)


if __name__ == "__main__":
    main()
