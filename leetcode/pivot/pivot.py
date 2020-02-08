

numbers = [1, 7, 3, 6, 5, 6]


def find_pivot(numbers):

    from_right = numbers[::-1]

    totals_from_left = 0
    totals_from_right = 0

    # for i, number_from_left in enumerate(numbers):
    #     totals_from_left += number_from_left
    #     # import pdb; pdb.set_trace()

    # for j, number_from_right in enumerate(from_right):
    #     totals_from_right += number_from_right

    index = 0
    while index <= len(numbers):
        for number_from_left in numbers:
            totals_from_left += number_from_left
            for number_from_right in from_right:
                totals_from_right += number_from_right
        if totals_from_left == totals_from_right:
            print(totals_from_left)
        index += 1
        

    
    
        

print(find_pivot(numbers))

















  # totals_from_left = []

    # totals_from_right = []

    # from_right = numbers[::-1]

    # for i, number_from_left in enumerate(numbers):
    #     next_num = numbers[(i+1) % len(numbers)]
    #     result = number_from_left + next_num
    #     totals_from_left.append(result)

    # for i, number_from_right in enumerate(from_right):
        
    #     next_num = from_right[(i+1) % len(numbers)]
    #     result = number_from_right + next_num
    #     # print(next_num)
       
    #     totals_from_right.append(result)

 