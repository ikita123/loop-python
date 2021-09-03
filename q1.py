num=int(input("enter number"))
sum=0
b=sum
order=len(str(num))
while num>0:
    digit=num%10
    sum=sum+(digit**order)
    print(sum)
    num=num//10
if sum==b:
    print(b,"is amstrong")
else:
    print(b,"is not amstrong")