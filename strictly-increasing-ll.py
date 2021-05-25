# https://binarysearch.com/problems/A-Strictly-Increasing-Linked-List
class Solution:
    def solve(self, head):
        if not head.next:
            return True

        current = head
        lastVal = current.val
        current = current.next

        while current:
            diff = current.val - lastVal
            if diff <= 0:
                print(diff)
                return False
            lastVal = current.val
            current = current.next

        return True
