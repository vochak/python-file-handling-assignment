# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Python is fun!\n")
    print("File 'my_file.txt' created successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of 'my_file.txt':\n")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
    print("\nFile 'my_file.txt' updated with additional lines.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("\nScript execution completed.")
