# Ask user for a number
# Sum of natural numbers till user's number
# Print total from 1 to n
n=input("Please enter a natural number : ")
n=int(n)
i=0
sum=0
if(n<0):
    print("Please enter a positive number")
else:
    while i<=n:
        sum +=i
        i+=1
    print(f"Sum of numbers from 1 to {n} is : {sum}")
