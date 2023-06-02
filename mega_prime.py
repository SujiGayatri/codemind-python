n=int(input())
f=0
d=0
p=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    while n>0:
        f=0
        m=n%10
        for j in range(1,m+1):
            if m%j==0:
                f+=1
        if f==2:
            p+=1
        d+=1
        n=n//10
    if d==p:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")