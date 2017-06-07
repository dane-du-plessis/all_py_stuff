a = list('this is my song to you, a longing that will never die')
b = []

for i in range(0,len(a)):
    if a[i] == 'e': continue
    b.append(a[i])

print(a)
print(b)
