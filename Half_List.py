x = int(input())
l = list(map(int,input().split()))
for i in range(x-1,(x//2)-1,-1):
    print(l[i],end=" ")
for j in range(0,x//2):
    print(l[j],end=" ")