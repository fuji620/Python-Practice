a = {"apple": 5, "banana": 2, "cherry": 8}

a_items = sorted(a.items(),key = lambda item: item[1])

for key, value in a_items:
    print(key,value)






# 練習門題
fruits = [("apple", 5), ("banana", 2), ("cherry", 8), ("grape", 4)]
fruits_a = sorted(a.items())
