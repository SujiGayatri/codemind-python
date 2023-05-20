n=int(input())
s=list(map(int,input().split()))
m=int(input())
for i in s:
    if i+m>=max(s):
        print("True",end=" ")
    else:
        print("False",end=" ")