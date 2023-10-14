s1,s2,s3,s4,s5=map(int,input().split())
x=(s1+s2+s3+s4+s5)//5
if(x>=90):
    print("Grade A")
elif(x>=80):
    print("Grade B")
elif(x>=70):
    print("Grade C")
elif(x>=60):
    print("Grade D")
elif(x>=40):
    print("Grade E")
elif(x<40):
    print("Grade F")