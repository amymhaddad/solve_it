

numbers = [1, 7, 3, 6, 5, 6]

def find_pivot(numbers):
    totals_from_left = []

    totals_from_right = []

    from_right = numbers[::-1]

    for i, number_from_left in enumerate(numbers):
        next_num = numbers[(i+1) % len(numbers)]
        result = number_from_left + next_num
        totals_from_left.append(result)

    for i, number_from_right in enumerate(from_right):
        next_num = numbers[(-1-i) % len(numbers)]

        print(next_num)
        # result = number_from_left + next_num
        # totals_from_right.append(result)
       
        



    
        

print(find_pivot(numbers))
