from posixpath import split


name,character=input("Please enter name and a acharacter separated by comma : ").split(",")
print(f"Your name is : {name.strip()}")
print(f"Character in given name count :{name.strip().lower().count(character.strip().lower())}")
