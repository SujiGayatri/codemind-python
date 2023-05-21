n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n-1,2):
    fre=a[i]
    val=a[i+1]
    for i in range(fre):
        l.append(val)
print(*l)