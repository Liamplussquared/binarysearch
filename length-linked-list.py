# https://binarysearch.com/problems/Length-of-a-Linked-List
class Solution:
    def solve(self, node):
        len = 0
        current = node
        while current:
            current = current.next
            len += 1
        return len