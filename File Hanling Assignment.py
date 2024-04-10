# File Creation
try:
    # Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing at least three lines of text to the file
        file.write("Line 1: My Name is Jonathan!\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome\n")
        print("File created and initial content written successfully.")
except IOError as e:
    print("Error:", e)
finally:
    file.close()

# File Reading and Display
try:
    # Reading the contents of "my_file.txt"
    with open("my_file.txt", "r") as file:
        # Displaying the contents on the console
        print("\nFile Contents:")
        for line in file:
            print(line.strip())  # Stripping newline characters for cleaner output
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    file.close()

# File Appending
try:
    # Opening "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text to the existing content
        file.write("Line 4: Appended line 1\n")
        file.write("Line 5: 54321\n")
        file.write("Line 6: Python is versatile\n")
        print("\nFile content appended successfully.")
except IOError as e:
    print("Error:", e)
finally:
    file.close()
