n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
l=[]
for i in range(a,b+1):
    l.append(i)
for i in x:
    if i not in l:
        c=c+i
print(c)