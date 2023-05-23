n=int(input())
s=list(map(int,input().split()))
x=sum(s)
b=0
c=x//n
for i in range(n):
    if s[i]<=c:
        b+=1
print(b)