num=int(input("enter number"))
a=0
b=1
i=1
c=0
while i<=num:
    c=a+b
    b=a
    a=c
    print(c)
    i+=1
