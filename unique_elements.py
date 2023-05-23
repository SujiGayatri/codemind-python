n=int(input())
s=list(map(int,input().split()))
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(*l)