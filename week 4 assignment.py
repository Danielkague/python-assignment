filename = input("Enter the filename: ")

try:
    # Open the file to read
    file = open(filename, "r")
    content = file.read()
    file.close()

    # Modify the content (make it uppercase)
    new_content = content.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    new_file = open(new_filename, "w")
    new_file.write(new_content)
    new_file.close()

    print("File was modified and saved as", new_filename)

except FileNotFoundError:
    print("Error: File not found.")
except:
    print("Something went wrong.")
