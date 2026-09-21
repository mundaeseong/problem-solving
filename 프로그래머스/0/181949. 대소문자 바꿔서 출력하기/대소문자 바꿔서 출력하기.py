str = input()
res = ""
for i in range(len(str)):
    if str[i].isupper():
        res += str[i].lower()
    else:
        res += str[i].upper()
print(res)
