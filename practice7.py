# Loops

# 1. While loop
i=1
while i<=5:
    print(i)
    i+=1
print("Loopd ended")

#print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1
print("Done")

#print numbers form 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
print("Done")

#print the multiplication table of a number n
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(num*i)
    i+=1

# print the element of the following list using a loop
list1=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list1):
    print(list1[idx])
    idx+=1

#Search for a number x in the tuple using loop

tuple1=(1,4,9,16,25,36,49,64,81,100)
x=49
i=0
while i<len(tuple1):
    if tuple1[i]==x:
        print("found ",x,"at",i)
    i+=1


#Break & continue
i=0
while i<=5:
    if(i==3):
       
        break
    i+=1
    print(i)


i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
    # print(i)

#for loop
# print the elements of the following list using a loop:
list1=[1,4,9,16,25,36,49,64,81,100]
for num in list1:
    print(num)

#Search for a number x in this tuple using loop
tuple1=(1,4,9,16,25,36,49,64,81,100)
x=64
for num in tuple1:
    if(num==x) :
        print("Found",x)
        break
    print(num)

#range
for i in range(2,10,2):
    print(i)

#print numbers from 1 to 100 
for i in range(1,101):
    print(i)
    
#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)


#print multiplicaton table for number n
num1=int(input("Enter a number:"))
for i in range(1,11):
    print(i*num1)

#WAP to find sum of first n numbers (using while )
n=int(input("Enter a number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)

#WAP to find the factorial of first n numbers (using for)
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
    i+=1
print(fact)