n=int(input())
c=0
for i in range(1,n//2):
    if (i*(i+1)==n):
        print("YES")
        c=1
if c==0:
    print("NO")