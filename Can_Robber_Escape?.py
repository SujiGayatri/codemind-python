n=int(input())
c=0
x=list(map(int,input().split()))
for i in range(n):
    if x[i]%2!=0:
        c+=1
if c<=2:
    print("YES")
else:
    print("NO")
