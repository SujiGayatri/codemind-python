n=int(input())
x=list(map(int,input().split()))
l=list(set(x))
c=0
for i in l:
    if i%2==0:
        c+=1
print(c)