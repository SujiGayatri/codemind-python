n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(len(l)):
    if i%2==0:
        s+=l[i]
    else:
        c+=l[i]
if (s-c)==0:
    print("YES")
else:
    print("NO")