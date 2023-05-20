n=int(input())
s=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if(s[i]==s[j]):
            c+=1
    if(c>n//2):
        print(s[i])
        s[i]=0