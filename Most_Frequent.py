n=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count=count+1
    if count>m:
        m=count
        k=arr[i]
    elif count==m and arr[i]<k:
        k=arr[i]
print(k)