num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

operation=input("Enter a operation you want to perform : ")
if(operation=="+"):
    print(num1+num2)
elif(operation=="-"):
    print(num1-num2)
elif(operation=="*"):
    print(num1*num2)
elif(operation=="/"):
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1/num2)
elif(operation=="%"):
    if num2 == 0:
        print("Cannot perform modulus by zero")
    else:
        print(num1%num2) 
else:
    print("Sorry can't perform this operation")