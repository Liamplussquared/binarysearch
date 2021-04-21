# https://binarysearch.com/problems/Unique-People-in-Contact-List
class Solution:
    def solve(self, contacts):
        emails = set()
        unique = True
        res = 0

        for contact in contacts:
            unique = True
            for email in contact:
                if email in emails:
                    unique = False
                else:
                    emails.add(email)
            if unique:
                res += 1

        return res
