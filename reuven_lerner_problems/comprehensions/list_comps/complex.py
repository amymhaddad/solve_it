"""
(1) Given a list of integers, use a list comprehension
    to calculate the sum of the factorials of those integers.

n! = n-1 * n-2 * n-3 ... 1

5! = 5 * 4 * 3 * 2 * 1

[3, 4, 5]

3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120

(+ 6 24 120)

(2) From mini-access-log.txt, create a list of the IP
    addresses in that file.

(3) Create a dictionary (or a variant thereof -- such
    as Counter) in which the keys are the IP addresses
    and the values are the number of times that each
    IP address appeared in the file.  Use the resulting
    dict/Counter to print each IP address and its times

(4) Create, from linux-etc-passwd.txt, a list of tuples
    in which each tuple is (username, user_id) .
    username is field index 0, user_id is field index 2
"""

# Exercise 1
# Option 1 (the expression in the function in the example)
def factorial(num):
    total = 1
    for i in range(num, 0, -1):
        total *= i
    return total


numbers = [3, 4, 5]
result = sum([factorial(num) for num in numbers])

# Option 2
def factorial_alt(num):
    if num <= 1:
        return num
    return num * factorial_alt(num - 1)


numbers2 = [3, 4, 5]
result2 = sum([factorial_alt(num) for num in numbers2])


# Exercise 2
addresses = [record.split()[0] for record in open("mini-access-log.txt")]

# Exercise 3
# Option 1:
from collections import Counter

ip_counts1 = Counter(addresses)

address_counts = [f"{address} -- {str(count)}" for address, count in ip_counts1.items()]

# Option 2:
ip_counts2 = Counter(line.split()[0] for line in open("mini-access-log.txt"))

for line, count in ip_counts2.items():
    print(f"{line:.<20}{str(count)}")


# Exercise 4
usernames_userIds = [
    tuple(user.split(":")[0:3:2])
    for user in open("linux-etc-passwd.txt")
    if user.strip() and not user.startswith("#")
]
