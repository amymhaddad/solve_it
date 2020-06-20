"""
I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated."
"""

def find_rotation_point(words):
    low = 0
    high = len(words) - 1

    while high - low > 1:
        mid = (low + high) // 2

        if words[mid] >= words[low]:
            low = mid
        else:
            high = mid
    return high
