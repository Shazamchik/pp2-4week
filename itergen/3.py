class nums:
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        x = self.n
        self.n+=1
        return x
mynum = nums()
myit = iter(mynum)
print(next(myit))
print(next(myit))
print(next(myit))