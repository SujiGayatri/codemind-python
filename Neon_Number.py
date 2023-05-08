n=int(input())
x=0
s=n*n
while s!=0:
    r=s%10
    x=x+r
    s=s//10
if n==x:
    print("Neon Number")
else:
    print("Not Neon Number")