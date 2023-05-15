n=int(input())
a=list(map(int,input().split()))
m=10**5
for i in range(n):
    if m>a[i]:
        m=a[i]
for i in range(1,m+1):
    c=0
    for j in range(0,n):
        if a[j]%i==0:
            c+=1
    if c==n:
        h=i
print(h)