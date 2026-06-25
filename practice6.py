# # Dictionary
std={
    "name": "Aamer",
    "Subject":{
        "python":30,
        "sql":29,
        "Excel":28
    },
    "id":302024
}

print(std["Subject"]["python"])
print(std.keys())
print(std.values())
print(std.items())
print(std.clear())
print(std.get("name"))
print(std.update({"gender": "male"}))
print(std.values())

#SET in python
set1={1,2,3,"Aamer","Shaikh"}
set2={2,3,4,5,6,}
set1.add(5)
print(set1.pop())
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)


#Store values in dictionar

dict1={
    "table":["a piece of furniture",
    "list of fatcs & figures"],
    "cat":"Small animal"
}

print(dict1)

sub={"python","java","c++","python","javascript"
     ,"java","python","java","c++","c"}
print("Classrooms needed for every (unique) subject are: ",len(sub))

'''
WAP to enter marks of 3 subjects from user and store thme in a dic .
Start with an empty dic & add one by one
Use subj name as key & marks as values '''

dic={}
marks1=int(input("enter the marks of phy: "))
dic.update({"phy":marks1})
marks2=int(input("enter the marks of phy: "))
dic.update({"chem":marks2})
marks3=int(input("enter the marks of phy: "))
dic.update({"maths":marks3})
print(dic)

# figure out a waty to store 9 & 9.0 as separate valuees in set
set1={('int',9),('float',9.0)}
print(set1)