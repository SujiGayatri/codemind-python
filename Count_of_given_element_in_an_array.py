n=int(input())
x=list(map(int,input().split()))
m=int(input())
c=0
for i in x:
    if i==m:
        c+=1
print(c)