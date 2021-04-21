# https://binarysearch.com/problems/Reverse-a-Linked-List
class Solution:
    def solve(self, node):
        prev, current, nxt = None, node, None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
