n=int(input())
m=int(input())
for i in range(n,m+1):
    s=0
    t=i
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if s==t:
        print(t,end=" ")