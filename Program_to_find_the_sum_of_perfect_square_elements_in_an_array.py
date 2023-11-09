import math
n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    a=int(math.sqrt(i))
    if a*a==i:
        l.append(i)
print(sum(l))