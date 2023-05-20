t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    for i in range(1,b+1):
        y=x[-1]
        x.remove(y)
        x=x[::-1]
        x.append(y)
        x=x[::-1]
    print(*x)