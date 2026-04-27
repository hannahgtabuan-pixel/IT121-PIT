def main():
    try:
        username = input("Enter username: ")
        age = int(input("Enter age: "))  # possible error if not a number

        if username.strip() == "":
            raise ValueError("Username cannot be empty.")
        if age <= 0:
            raise ValueError("Age must be a positive number.")