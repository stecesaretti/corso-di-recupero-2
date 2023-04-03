#l'utente deve scegliere mare lago o campagna
print("1.mare")
print("2.lago")
print("3.campagna")
a = int(input("Dove vuoi andare? >"))
if a == 1:
    print("Vai al mare")
elif a == 2:
    print("Vai al lago")
else :
    print("Vai in campagna")