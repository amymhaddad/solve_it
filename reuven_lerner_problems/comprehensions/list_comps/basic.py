# Ex 1
mylist = [10, 20, 30]
update_list1 = "".join([str(num) + "*" for num in mylist])
update_list2 = "*".join([str(num) for num in mylist])

# Ex 2
hex_nums = input("Enter some hex nums: ").split()
total2 = sum([int(char, 16) for char in hex_nums])

# Ex 3
user_input3 = "this is a test"
count = sum([1 for char in user_input3 if char.isalpha()])
