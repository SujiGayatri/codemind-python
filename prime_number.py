def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
n=int(input())
if prime(n)==2:
    print("prime")
else:
    print("not a prime")