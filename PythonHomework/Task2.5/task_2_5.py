str1 = input("Input str1")
str2 = input("Input str2")
s1 = list(str1)
s2 = list(str2)
if len(str1) == len(str2):
    x = 0
    for i in range(len(s1)):
        for k in range(len(s2)):
            if s1[i] != s2[i]:
                print("strings are not equal")
                x = 1
                break
    if x != 1:
        print("strings are equal")
else:
    print("strings are not equal")
    x = 0
    for i in range(len(str1) - len(str2) + 1):
        if str2 == str1[i: i + len(str2)]:
            print("str2 is substring str1")
            x = 1
            break
    if x != 1:
        print("str2 is not substring str1")
for i in range(int(len(s1)/2)):
    if s1[i] != s1[-i-1]:
        print("str1 is not palindrome")
        x = 2
        break
if x != 2:
    print("str1 is palindrome")
