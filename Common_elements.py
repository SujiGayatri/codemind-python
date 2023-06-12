n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d=[]
for i in x:
    if i in y and i not in d :
        d.append(i)
print(*d)