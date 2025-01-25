from collections import Counter


a = [1, 2, 3, 1, 2, 1, 4, 5, 2]
c = dict(Counter(a))
print(c)