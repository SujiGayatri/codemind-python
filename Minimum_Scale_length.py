n=int(input())
a=list(map(int,input().strip().split()))
m=max(a)
for i in range(m,0,-1):
    c=0
    for j in range(n):
        if(a[j]%i==0):
            c=c+1
    if(c==n):
        print(i)
        break