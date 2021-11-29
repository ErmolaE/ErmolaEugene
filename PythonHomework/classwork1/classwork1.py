d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'tvelve': 12, 'thirteen': 13, 'fourteen': 14,'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
l = ("five thirteen two eleven seventeen two one thirteen ten four eight five nineteen").split()
l = list(d[x] for x in l)
print(l)

l = list(set(l))
print(l)

#сортировка, как я понял, уже не нужна:
#for i in range(len(l)-1):
#    k = i
#    t = i+1
#   while t < len(l):
#        if l[k] >= l[t]:
#            k = t
#        t += 1
#    l[i], l[k] = l[k], l[i]
#print(l)

m = []
for i in range(len(l)-1):
    if i % 2 == 0:
        m.append(l[i]*l[i+1])
    if i % 2 != 0:
        m.append(l[i]+l[i+1])
print(m)

s = 0
for i in range(len(l)):
    if l[i] % 2 != 0:
        s = s+l[i]
print(s)
