# Watch Coco
# Ask user name and Age
# If username starts with ('A' or 'a') and age is above 10 then print You can watch coco movie
# Else print Sorry, you cannot eatch coco
name,age=input("Please enter your name and age separated by ',': \n").split(",")
age=int(age)
if (name[0]=='a'or name[0]=='A')and age>=10:
    print("You can watch coco movie")
else:
    print("Sorry, you cannot watch coco")