string="is she is beautiful and she is good dancer"
print(string.replace("is","was",2))

# find: to search word's or char's pos in string
print(string.find("is"))
# print(string.find("is",7))
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)