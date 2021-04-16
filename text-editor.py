# https://binarysearch.com/problems/Text-Editor
class Solution:
    def solve(self, s):
        n, lst, i = len(s), [], 0

        while i < n:
            c = s[i]
            if c == "<":
                if i + 1 < n and s[i + 1] == "-":
                    if lst:
                        lst.pop()
                    i += 1
                else:
                    lst.append(c)
            else:
                lst.append(c)
            i += 1

        return "".join(lst)
