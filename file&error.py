def main():
    try:
        username = input("Enter username: ")
        age = int(input("Enter age: "))  # possible error if not a number

        if username.strip() == "":
            raise ValueError("Username cannot be empty.")
        if age <= 0:
            raise ValueError("Age must be a positive number.")
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

        print("\nSaved successfully!\n")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    finally:

        try:
            print("\n--- Saved Users ---")
            with open("users.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No users saved yet.")

        print("\nSystem complete.")



main()