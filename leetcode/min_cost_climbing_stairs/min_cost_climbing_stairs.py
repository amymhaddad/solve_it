"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
"""


def min_cost_climb_stairs(cost):

    len_costs = len(cost)
    if len_costs == 1:
        return cost[0]

    total_counts = [0] * len_costs

    total_counts[-1] = cost[-1]
    total_counts[-2] = cost[-2]

    for i in range(len_costs - 3, -1, -1):
        total_counts[i] = min(
            cost[i] + total_counts[i + 2], cost[i] + total_counts[i + 1],
        )

    if total_counts[0] > total_counts[1]:
        return total_counts[1]
    else:
        return total_counts[0]
