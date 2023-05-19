x=int(input())
y=int(input())
s=0
for i in range(0,x):
    a=list(map(int,input().split()))
    s=s+sum(a)
print(s)