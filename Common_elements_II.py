n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in x:
    if i not in y:
        print(i,end=' ')
for i in y:
    if i not in x:
        print(i,end=' ')      