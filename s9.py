x=input()
l,d=0,0
for i in x:
    if i.isalpha():
        l+=1
    if i.isdigit():
        d+=1
print("{0},{1}".format(l,d))