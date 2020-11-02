n=int(input("n:"))
suma=0
for x in range(1,n):
    if x%3==0 and x%5==0:
        suma+=x
print (suma)