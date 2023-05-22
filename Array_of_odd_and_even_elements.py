n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    if i%2!=0:
        l.append(i)
for i in x:
    if i%2==0:
        l.append(i)
print(*l)