#List and it's functions

list=[8,9,0,3,6]
print(list.append(1))
print(list.insert(4,4))
print(list.pop(4))
print(list.sort())
print(list.reverse())
print(list)

#Tuples and it's methods
tup=(1,2,3,4)
print(tup)
print(type(tup))
print(tup.count(3))
print(tup.index(1))

# WP to ask user to enter names of their 3 favourite movies & store them in a list
list=[]
movie1=input("Enter movie  1st name: ")
list.append(movie1)
movie2=input("Enter movie 2nd name: ")
list.append(movie2)
print(list)
print(type(list))


#WAP to check if a list contains a palindrom of elemnets.
list=[1,2,3,2,1]
list1=list.copy()
list1.reverse()

if(list==list1):
    print("palindrom exist")
else:
    print("it doesn't")

print(list)
print(list1)

#WAP to count the number of A in the following tuple
tup=('c','d','a','a','b','b','a',)
print(tup.count('a'))

#store the above value in a list & sort them from "A" to "D"
list=['c','d','a','a','b','b','a']
list.sort()
print(list)
