"""
(1) Ask the user to enter some integers, separated by
    spaces.  Sum the different numbers they enter.

    1 2 3   #  6
    1 2 3 1 2 3 # 6

(2) From the file nums.txt, sum all of the distinct numbers
    there.

(3)p

"""
# Exercise 1
user_input = input("Enter numbers: ").split()
total = sum({int(num) for num in user_input})

# Exercise 2
num_file = {int(num.strip()) for num in open("nums.txt") if num.strip()}


# Exercise 3
shells = {
    line.rstrip().split(":")[-1]
    for line in open("linux-etc-passwd.txt")
    if line.strip() and not line.startswith("#")
}
