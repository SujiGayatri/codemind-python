a,b,c=map(int,input().split())
x=0
while a!=b+1:
    if a%c==0:
        x+=1
    a+=1
print(x)