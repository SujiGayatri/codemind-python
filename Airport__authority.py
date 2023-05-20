n=int(input())
s=0
c=[]
for i in range(n):
       m=int(input())
       c.append(m)
t=int(input())
for k in c:
    if k<=t:
       s=s+1
    else:
       s=s+2
print(s)