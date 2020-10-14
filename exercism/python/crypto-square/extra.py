


"""
col 1 has 2 possible row pairs: (0, 1)
col 2 has 2 possbile row pairs: (1, 2)

c r
1 0
1 1
2 1
2 2
3 2
3 3
4 3
4 4

-First I create "row" numbers that could satisfy the 2 conditions
-Then I sub those numbers into the cond to see what works
# # For each value in the outer for loop i need to do 2 things: see if c >= r and c-r <= 1

# IF i put "row" on the outside of the loop, then it gets updated on each iteration of loop.
# BUT if I put it on the inside, then it only gets updated on after the completion of each loop

#col is continuously updated -- which is what I want it to do. BUT row is reset each time -- after the completion of each inner loop.
 
"""