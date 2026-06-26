operations=('1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulo\n6.Exit')
print(operations)
while True:
    op=int(input("select an operation: "))
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    if(op==1):
        print(num1+num2)
       
    elif(op==2):
        print(num1-num2)
        
    elif(op==3):
        print(num1*num2)
        
    elif(op==4):
        print(num1/num2)
        
    elif(op==5):
        print(num1%num2) 
        
    elif(op==6):
        print("Thanks for using our calculator")

    elif op<0:
        print("please selcet the correct number of operation")

    elif(op>6):
        print("please selcet the correct number of operation")
    
    w=input("Do you want to continue :y/n --> ")
    
    if(w=="n"):
        print("Thanks for using our calculator")
        break
