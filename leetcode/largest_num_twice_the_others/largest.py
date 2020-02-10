numbers = [3, 6, 1, 0]

def get_number(numbers):
    
    max_number = max(numbers)
    
    numbers_values = {}
    for i, num in enumerate(numbers):
        # import pdb; pdb.set_trace()
        if max_number <= num * 2:
            return -1
        else:
            if max_number == num:
                numbers_values[max_number] = i
    print(numbers_values)
        
        

print(get_number(numbers))