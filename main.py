# Step 1: Open the file in read mode and print its contents
with open('Sample_File.txt', 'r') as file:
    print("Contents of the file (before operations):")
    print(file.read())

# Step 2: Open the file in write mode and overwrite with a brief introduction
with open('Sample_File.txt', 'w') as file:
    file.write("Hi there! I am an AI program designed to help with coding, learning, and problem-solving.\n")

# Step 3: Open the file in append mode and add your favorite subject
with open('Sample_File.txt', 'a') as file:
    file.write("My favorite subject is Artificial Intelligence.\n")

# Step 4: Reopen the file in read mode and print its updated contents
with open('Sample_File.txt', 'r') as file:
    print("\nContents of the file (after operations):")
    print(file.read())

print("\nFile operations completed successfully!")
