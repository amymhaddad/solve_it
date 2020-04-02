list_string = ["A", "B", "C", "D"]


def reverse(list_string):

    left = -1
    right = 0

    if len(list_string) <= 1:
        return list_string

    # if list_string[left] == list_string[right]:
    #     break
    # elif len(list_string) // 2 == right:
    #     break
    # else:
    # import pdb

    # pdb.set_trace()

    list_string[left], *_, list_string[right] = list_string

    # import pdb

    # pdb.set_trace()

    # right += 1
    # left -= 1
    print(list_string)


print(reverse(list_string))
