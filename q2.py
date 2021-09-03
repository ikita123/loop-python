num=int(input("enter number"))
i=0
count=0
while i<num:
    if i%2==0:
        print(i)
        count=count+1
    i=i+1
print(count)