n=int(input("n:"))
s1,s2,s3,s4,s5,s6=0,0,1,0,0,3                   
factorial=1
for x in range(1,n): 
    s1+=x
    s2+=(x-1)*x
    s5+=x/(x+1)
    s6+=(20+x)
lista1=[x for x in range(1,(n*10)+1) if x%10==0]
for x in lista1:
  s4+=(x+2)
for x in range(2,n):
    factorial*=x
    s3+=factorial
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)
