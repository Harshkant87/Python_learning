user_input = input("Enter your name: ")
message = "Hello %s" % user_input
print(message)

# 1. f string method
user_input = input("Enter your name: ")
message = f"Hello {user_input}"
print(message)

# 2. Multiple variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = "Hello %s %s" % (name, surname)
print(message)

# 3. Multiple variables with f string
name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = f"Hello {name} {surname}"
print(message)


