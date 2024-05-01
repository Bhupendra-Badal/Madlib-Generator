print("Welcome to MADLIB.")
def madlib():
    noun = str(input("Enter any noun words: "))
    verb = str(input("Enter any verb words: "))
    noun1 = str(input("Enter the second noun: "))
    noun2 = str(input("Enter the third noun: "))

    madlibs = f'''
    Hey! My name is {noun}.
    Welcome to my {verb}.
    Here, I am with {noun1}.
    Come and enjoy with {noun2}.'''
    return madlibs
    
print(madlib())

print("Do you want to play Again.Yes or No")
choice = str(input("Enter your choice: " ))
if choice == "Yes":
    madlib()  
else:
    print("Thank you for playing.")