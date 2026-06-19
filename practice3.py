'''
  Write a Python function that accepts two integer numbers.
  If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
'''

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# if(num1*num2<=1000):
#     print(num1*num2)
# else:
#     print(num1+num2)


#WAP to heck if the entered nubmer is odd or even
# num= int(input("Enter a number: "))
# num1=num%2

# if(num1==0):
#   print("The number is even")
# else:
#    print("it's an odd number")

#WAP to find the greatest of 3 number entered by the user
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# num3=int(input("Enter 3rd number: "))

# if(num1>num2):
#     print("the greatest num is: ",num1)
# elif(num2<num3):
#     print("The greatest num is: ",num3)
# else:
#     print(num2," is greatest")

#WAP to ccheck if a number is a multiple of 7 or not
num=int(input("enter a number: "))
num1=num%7
if(num1==0):
    print("it's a multiple of 7")
else:
    print("it's not")