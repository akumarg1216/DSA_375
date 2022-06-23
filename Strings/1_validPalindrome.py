s = "0P"
s = s.lower()
str = ""
for i in s:
    if ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57:
        str=str+i

print(str[::-1])
if str == str[::-1]:
    print("true")
else:
    print("false")

print(str)