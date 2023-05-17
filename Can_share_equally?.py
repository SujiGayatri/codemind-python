a,b=map(int,input().split())
r=0
r=a-2*b
if a==0 and b%2==0:
    print("YES")
elif a==0 and b%2!=0:
    print("NO")
elif r%2==0:
    print("YES")
else:
    print("NO")