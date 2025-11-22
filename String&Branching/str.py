##
##st=str(input("enter the string: "))
##count=0
##size=len(st)
##print(size)
##for i in range(len(st)):
##        if st=="":
##            
##            break
##        if(i==0):
##            
##            print(st[i])
##            
##        if(i==size-1):
##            print(st[size-1])
##  

##s=str(input("enter the string: "))
##flag=False
##for i in range(len(s)):
##    if s[i]=='a':
##        print("YES")
##        flag = True
##        break
##
##if flag == False:
##    print("NO")

marks=int(input("Enter your marks for grading: "))
if(marks<=35):
    print("fail")
    
elif(50<marks<=60):
    print("E")
elif(60<marks<=70):
    print("D")
elif(70<marks<=80):
    print("C")
elif(80<marks<=90):
    print("B")
elif(90<marks<=100):
    print("A")
else:
    print("invalid marks")
