from random import randint
l=list()
for x in range (10):
    a=randint(1,100)
    l.append(a)
cont= 0
for z in l :
    if z > 30:
        cont+=1
print(l)
print(cont)