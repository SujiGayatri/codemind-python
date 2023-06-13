n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=set(x)
b=set(y)
c=0
for i in a:
    if i not in b:
        c+=1
for i in b:
    if i not in a:
        c+=1
print(c)