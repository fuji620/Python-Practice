A = {"apple", "banana", "cherry"}
B = {"apple", "cherry", "orange"}


common = A & B
oll = A | B

jaccard = len(common) / len(oll)

print(jaccard)