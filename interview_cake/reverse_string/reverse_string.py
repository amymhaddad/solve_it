list_string = ["A", "B", "C", "D"]


def reverse(list_string):

    left = -1
    right = 0

    if len(list_string) <= 1:
        return list_string

    while True:
        # import pdb

        # pdb.set_trace()
        # Update this test to account for when all letters ahve been reversed and only have a middle char
        if left + right <= 1:
            break

        elif len(list_string) // 2 == right:
            break

        else:
            list_string[left], *_, list_string[right] = list_string

            right += 1
            left -= 1
    return list_string


print(reverse(list_string))
