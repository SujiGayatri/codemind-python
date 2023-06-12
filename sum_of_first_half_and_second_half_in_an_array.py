n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in range(n//2):
    s+=x[i] 
print(s)
for j in range(n//2,n):
    c+=x[j]
print(c)