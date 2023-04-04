from random import randint
l=[]
for x in range (10):
    a= randint(1,100)
    l.append(a)
s= 0
for z in l:
    s+=z
print(l)
print(s)
