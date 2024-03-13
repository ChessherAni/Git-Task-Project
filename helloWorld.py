user_message = input("What would you like to print: ")

while True:
    if user_message != "" and user_message != " ":
        break
    else:
        user_message = input("Input something that will be seen: ")
print(user_message)