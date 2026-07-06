# Create a new file using python add the following data

f=open("practice.txt","r")
f.write("hi everyone \nwe are learning file I/O \nusing python.\nI like programing in python")

# WAP to replace python to java
data=f.read()
new_data=data.replace("python","java")

f=open("practice.txt","w")
f.write(new_data)

# Search if the learning exists or not
print(data.find("learning"))

#Wap to find the in which learning word exists
def check_for_line():
    word="java"
    line_no=1
    data=True
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
            line_no+=1
    return -1        
check_for_line()


# Wap from a file containing numbers seperated by comma, print the count of even numbers

def count_of_even():
    data=True
    count=0
    with open("practice.txt","r")as f:
        data=f.read()
        num=data.split(",")
        for val in num:
            if(int(val)%2==0):
                count+=1
    print(count)            

count_of_even()

      
