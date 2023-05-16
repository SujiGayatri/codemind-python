a=list(map(int,input().split(',')))
x=[]
for i in range(len(a)):
    s=0
    for j in range(1,(a[i]+1)):
        if a[i]%j==0:
            s+=j
    if s in a:
        x.append(a[i])
x=sorted(x)
for i in x:
    print(i,end=' ')
if len(x)==0:
    print("-1")