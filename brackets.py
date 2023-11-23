def is_ceq(ceq):
    control = []
    for br in ceq:
        if br in '([{':
            control.append(br)
        else:
            if not control:
                return False
            open_br = control.pop()
            if br == ')' and open_br != '(':
                return False
            if br == ']' and open_br != '[':
                return False
            if br == '}' and open_br != '{':
                return False
    return not control


def main():
    br_seq = input()
    result = is_ceq(br_seq)
    print(result)


if __name__ == '__main__':
    main()
