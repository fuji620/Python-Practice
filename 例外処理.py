try:
    print(1/0)
except ZeroDivisionError:
    print("間違ってるよ")



s = "apple"

try:
    print(s[5])
except IndexError:
    print("スペルミス")