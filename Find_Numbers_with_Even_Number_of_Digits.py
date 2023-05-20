n=int(input())
c=0
x=0
a=list(map(int,input().split()))
for i in range(len(a)):
       c=0
       while(a[i]):
            d=a[i]%10
            c+=1
            a[i]=a[i]//10
       if(c%2==0):
             x+=1
print(x)