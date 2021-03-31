# https://binarysearch.com/problems/Search-in-a-Virtually-Complete-Binary-Tree
class Solution:
    def solve(self, root, target):
        if not root:
            return False

        # Obtain path that must be followed to find number
        temp = target
        path = []
        while temp > 1:
            if temp % 2 == 0:
                path.append("l")
            else:
                path.append("r")
            temp //= 2

        # Follow path in tree and see if target is found
        current = root
        while len(path) > 0 and current:
            direction = path.pop()
            if direction == "l":
                current = current.left
            elif direction == "r":
                current = current.right

        if not current:
            return False

        return current.val == target



