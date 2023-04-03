from random import randint
#primo giocatore
a=randint(1, 6)
b=randint(1, 6)
i=1
while a != b:
    a= randint(1, 6)
    b= randint(1, 6)
    i+=1
    print(a, b)
print (i)
#secondo giocatore
a=randint(1, 6)
b=randint(1, 6)
i1= 1
while a != b:
    a= randint(1, 6)
    b= randint(1, 6)
    i1+=1
    print(a, b)
print(i1)
#conteggio finale
if i<i1:
    print("Giocatore 1 ha vinto")
elif i == i1:
    print("pareggio")
else:
    print("Giocatore 2 ha vinto")