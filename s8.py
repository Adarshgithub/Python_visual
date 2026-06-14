x=input().split()
for i in x:
    if x.count(i)>1:
        x.remove(i)
x.sort()
print(' '.join(x))