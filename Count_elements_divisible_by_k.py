n,m=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in x:
    if i%m==0:
        c+=1
print(c)