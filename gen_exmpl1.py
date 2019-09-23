def example(l):
    yield l

a=example([1,2,4])
print(a)
print(a.__next__())