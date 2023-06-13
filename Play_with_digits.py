n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    while i:
        r=i%10
        s+=r
        i=i//10
print(s)