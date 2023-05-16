a=int(input())
b=int(input())
x=[]
c=0
for i in range(a,b+1):
    x.append(i)
for i in range(len(x)):
    s=0
    for j in range(i,len(x)):
        s=s+x[j]
        if s%2==1:
            c+=1
print(c)