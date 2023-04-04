from random import randint
l=[]
for x in range (10):
    a= randint(1,100)
    l.append(a)
print (l)
cont=0
for z in l:
    if z>30 and z<70:
        cont+=1
print (cont)
