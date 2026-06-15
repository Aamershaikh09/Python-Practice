# Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.
a = 34
b = 80

c=a<b
print(c)


# Write a python program to find an average of two numbers entered by the user.
num1=int(input("Enter number first: "))
num2=int(input("Enter second number :"))
avg=(num1+num2)/2
print("The average of given 2 numbers is :",avg)

# Write a python program to calculate the square of a number entered by the user
num1=int(input("Enter a number: "))
square=num1*num1
print("The of number is : ",square)

# Write a python program to display a user entered name followed by Good Afternoon using input() function.
name=input("Enter your name: ")
print(name,"Good afternoon")

# Write a program to detect double space in a string
str=input("Enter a string: ")
count=str.count("  ")
print(count)

#Replace the double space from problem 3 with single spaces.
str=input("Enter a string with 2 spaces: ")
repl=str.replace("  ","   ")
print(repl)
count=repl.count("   ")
print(count)