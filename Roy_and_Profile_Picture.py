l=int(input())
t=int(input())
for i in range(1,t+1):
    w,h=map(int,input().split())
    if w<l or h<l:
        print('UPLOAD ANOTHER')
    elif w==h:
        print('ACCEPTED')
    else:
        print('CROP IT')