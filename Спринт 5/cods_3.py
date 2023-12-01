"""
ССЫЛКА НА КОНТЕСТ:
https://contest.yandex.ru/contest/53748/problems/
"""


# A. Камни с Марса
def sorting(len_el: int, els: list, len_smpl_el: int, smpl_el: list):
    els.sort()
    smpl_el.sort()

    zero_sotr = 0
    sample_index = 0

    for el in els:
        while sample_index < len_smpl_el and smpl_el[sample_index] < el:
            sample_index += 1
        if sample_index < len_smpl_el and smpl_el[sample_index] >= el:
            zero_sotr += 1
            sample_index += 1

    return zero_sotr


def main():
    len_element = int(input())
    elements = list(map(int, input().split()))
    len_sample_element = int(input())
    sample_element = list(map(int, input().split()))
    result = sorting(len_element, elements, len_sample_element, sample_element)
    print(result)


if __name__ == '__main__':
    main()
