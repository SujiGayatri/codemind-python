n=int(input())
a=0
b=1
x=0
for i in range(n+1):
    c=a+b
    if c==n:
        x+=1
        break
    a=b
    b=c
if x!=0:
    print("True")
else:
    print("False")