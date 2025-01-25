from collections import Counter


b = ["apple", "banana", "apple", "cherry", "cherry", "cherry", "banana", "apple", "apple", "cherry"]
fruit_b = dict(Counter(b))
fruit_count = dict(sorted(fruit_b.items(),key = lambda item:item[1]))

print(fruit_count)
