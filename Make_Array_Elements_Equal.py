a=int(input())
x=list(map(int,input().split()))
if (len(set(x))==1):
    print(0)
else:
    c=m=0
    for i in range(a):
        c=0
        for j in range(i,a):
            if x[i]==x[j]:
                c+=1
                if m<c:
                    m=c
    print(m)