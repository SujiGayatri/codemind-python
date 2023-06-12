n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x,y=set(x),set(y)
c=0
for i in x:
    if i in y:
        c+=1
print(c)