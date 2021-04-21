# https://binarysearch.com/problems/Level-Order-Traversal
class Solution:
    def solve(self, root):
        q, res = [], []
        q.append(root)

        while len(q) > 0:
            res.append(q[0].val)
            current = q.pop(0)

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        return res
