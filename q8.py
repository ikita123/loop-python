i=2
sum=0
user= int(input("enter number"))
while i>user:
    if user%i==0:
        print(i)
        sum=sum+1
    i=i+1
if sum==2:
    print("it is perfect number")
else:
    print("it is not perfect number")