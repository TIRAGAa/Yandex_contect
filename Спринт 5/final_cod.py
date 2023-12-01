"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/53750/problems/
"""


# A. Шифрованные инструкции
def parsing_comand(comand: str):
    stack = []
    cur_num = 0
    sub_str = []

    for symbol in comand:
        if symbol.isdigit():
            cur_num = cur_num * 10 + int(symbol)
        elif symbol == '[':
            stack.append((cur_num, sub_str))
            cur_num = 0
            sub_str = []
        elif symbol == ']':
            num, prev_str = stack.pop()
            sub_str = prev_str + [''.join(sub_str) * num]
        else:
            sub_str.append(symbol)

    return ''.join(sub_str)


def main():
    comand = input()
    resulr = parsing_comand(comand)
    print(resulr)


if __name__ == '__main__':
    main()
