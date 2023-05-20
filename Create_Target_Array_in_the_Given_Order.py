n=int(input())
t=[]
l=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
for i in range(n):
     t.insert(b[i],l[i])
for i in range(n):
     print(t[i],end=' ')
