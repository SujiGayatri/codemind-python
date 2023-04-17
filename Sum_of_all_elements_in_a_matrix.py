n,m=map(int,input().split())
s=0
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
for i in m:
     s=s+sum(i)
print(s)