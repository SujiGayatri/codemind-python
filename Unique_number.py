n=int(input())
s=str(n)
st=set(s)
if len(s)==len(st):
    print( 'Unique Number')
else:
    print('Not Unique Number')