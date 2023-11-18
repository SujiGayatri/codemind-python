n=int(input())
x=list(map(int,input().split()))
a=int(input())
c=0
for i in x:
    if a==i:
        c+=1
        break
if(c==1):
    print("True")
else:
    print("False")