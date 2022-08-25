# Take 2 comma separated input from user
# 1) User's name
# 2) A single character

# Output : Print 2 lines
# 1) User's name length
# 2) Count the character occurance in user's name but case insensitive
name,character=input("Please enter your name and a character seaparated by commas: \n").split(",")
print(f"Length of your name is: {len(name)}")
print(f"Occurance of character in String is: {name.lower().count(character.lower())} times")