# String and conditional statements
# str1="Aamer"
# str2="Shaikh"
# print(str1+str2) #concatinating
# print(str1[4]) #indexing

#slicing
# str3="Shaikh_Aamer"
# print(str3[1:5]) #1 to 5 but does not print 5th indexed value
# print(str3[0:12]) # 0 to 12(last)
# print(str3[:12]) # start from 0 to 12th
# print(str3[0:]) # start with 0 till 12th
# print(str3[-5:-1]) 

#functions
# str4="hello wolrd"
# print(str4.endswith("d")) # checks if string ends with given value
# print(str4.capitalize()) # capitalize the string
# print(str4.replace("l","L")) # replace the given value
# print(str4.count("l")) #count the occurance of the word
# print(str4.find('l')) #returns 1st index of 1st occurance


# # WAP to input user's first name & print it's length
# str=input("Enter your name: ")
# print(str)
# print("The length of given string is: ",len(str))

# WAP to find the occurance '$' in a string
# str="hi $my name is$ $ame$ sha$ikh"
# print("The number of occurance of the '$' is:",str.count("$"))

# # conditional statement
# age=21
# if(age>=18):
#     print("You can vote")
# elif(age>100):
#     print("how the fuck are you even alive dude")
# else:
#     print("You can't vote")



# marks=int(input("Enter your marks: "))

# if(marks<35):
#     print("You failed buddy")
# elif(marks>90):
#     print("You have topped")
# elif(marks>100):
#     print("Are you serious right now bro")
# else:
#     print("pass")

num=20
a=num%2
print(a)