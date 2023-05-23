n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    if x[i]!=0 and x[i]!=1:
        print("False")
        break
else:
    print("True")