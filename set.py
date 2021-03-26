#https://binarysearch.com/problems/Set
"""
Implementing a hashset would be ideal
I just used a set to create another set
"""
class CustomSet:
    def __init__(self):
        self.lst = set()

    def add(self, val):
        if not self.exists(val):
            self.lst.add(val)

    def exists(self, val):
        return val in self.lst

    def remove(self, val):
        if self.exists(val):
            self.lst.remove(val)
