n=int(input())
s=list(map(int,input().split()))
e=0
o=0
for i in range(n):
     if i%2==0:  
         o+=s[i]
     else:
         e+=s[i]
if(o-e==0):
     print("YES")
else:
     print("NO")