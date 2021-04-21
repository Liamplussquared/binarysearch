# https://binarysearch.com/problems/Hash-Table
class HashTable:
    def __init__(self):
        self.table = {}

    def put(self, key, val):
        self.table[key] = val

    def get(self, key):
        if key in self.table:
            return self.table[key]
        return -1

    def remove(self, key):
        if key in self.table:
            self.table.pop(key)
