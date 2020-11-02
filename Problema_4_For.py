a=int(input("a:"))
b=int(input("b:"))
if a<b:
    lista=[x for x in range(a,b) if x%2!=0]
    for x in lista:
        print(x)