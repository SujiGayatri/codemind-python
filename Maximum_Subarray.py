n=int(input())
a=list(map(int,input().split()))
s=a[0]
c=a[0]
for i in range(1,n):
    c=max(a[i],c+a[i])
    s=max(s,c)
print(s)