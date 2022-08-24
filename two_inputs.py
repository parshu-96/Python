# name=input("Enter your name : ")
# age=input("Enter your age : ")
#Aim is to take 2 inputs in one line
# name,age=input("Enter your name and Age : ").split()
# print("Name :"+name)
# print("Age :"+str(age))

name,age=input("Enter your name and Age : ").split(",") #To change Space as separator to comma as separator
print("Name :"+name)
print("Age :"+str(age))