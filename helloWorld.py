# ask for user input
user_message = input("What would you like to print: ")

# check that the user didn't enter a newline or space
while True:
    if user_message != "" and user_message != " ":
        break
    # prompt user until valid input is given
    else:
        user_message = input("Input something that will be seen: ")

# print user input
print(user_message)