"""
    The ide of it was to build it with one liner ;)
"""

class Solution:
    replaceElements = lambda self, arr: [max(arr[i+1:]) if i < len(arr) -1 else -1
                                         for i, num in enumerate(arr)]
