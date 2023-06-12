n=int(input())
x=list(map(int,input().split()))
m=int(input())
s=0
for i in x:
    if i<=m:
        s+=i
print(s)