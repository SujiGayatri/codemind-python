x=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l.reverse()
k=[]
for i in range(len(l)):
    if i%2!=0:
        k.append(l[i])
        k.append(l[i-1])
if(x%2==1):
    k.append(l[x-1])
print(*k)