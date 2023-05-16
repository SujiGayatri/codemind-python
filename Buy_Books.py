n=int(input())
a=map(int,input().split())
b=map(int,input().split())
x=sum(a)
y=sum(b)
if x-y>0:
    print("0")
else:
    print(y-x)