a=[]
j=20
while j>0:
    num=int(input("enter number"))
    a.append(num)
    j=j-1
print(a)
even=0
odd=0
positive=0
negative=0
zero=0
j=19
while j>=0:
    if a[j]<0:
        negative=negative+1
    elif a[j]>0:
     positive=positive+1
    elif a[j]==0:
        zero=zero+1
    if a[j]%2==0:
        even=even+1
    else:
        odd=odd+1
    j=j-1
print("even",even)
print("odd",odd)
print("positive",positive)
print("negative",negative)
print("zero",zero)
    










