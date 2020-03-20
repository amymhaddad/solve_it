"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

strs = ["a", "a", "b"]


def longest_common_prefix(strs):

    if not strs:
        return ""

    if len(strs) <= 1:
        return strs[0]

    shortest_word = min(strs, key=len)
    if not shortest_word:
        return ""

    i = 0

    while i < len(shortest_word):

        char = shortest_word[i]

        for word in strs:
            if word[i] != char:
                return word[:i]

        i += 1

    return shortest_word[:i]
