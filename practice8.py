# make a function whic returns avg or 3 no.
def avg(a,b,c):
    avgg=(a+b+c)/3
    print(avgg)

avg(10,20,30)
avg(1,2,3)

#WPA to print length of a list
list1=[1,2,3,4,5,6,"a"]

def lengthh():
     return len(list1)

print(lengthh())

#WAP to print the element of a list in a single line 
list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6,"a","b","c"]

def print_list(list):
    for item in list:
        print(item,end=" ")

print(print_list(list1))

#WAP to calculate factorial
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

fac(7)

#WAP to convert USD to INR (30-06-26 / 1$=94.674 rs)
def usd(n):
    inr=n*94.675
    print(inr)
usd(10)

#WPA which takes a input if it's odd it says odd 
num=float(input("Enter a number: "))

def detect(num):
    if (num%2==0):
        print("Even")
        return "even"
    else:
        print("Odd")
        return "odd"
    print(detect)

detect(num)

# recursion
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print("End")
show(5)

# # factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

#Write a recursive function to calculate the sum of first n natural numbers

def sum_of_n(n):
    if(n==0):
        return 0
    return sum_of_n(n-1)+n
print(sum_of_n(5))


#WAR function to print all element in a list
list1=[1,2,3,4,5,6,7,8,"a","b"]

def print_list(list,idx=0):
    if (idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

print_list(list1,7)