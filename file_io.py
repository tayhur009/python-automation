# Create and write to a file
with open("sample.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("It has multiple lines.\n")

# Read from the file
with open("sample.txt", "r") as f:
    contents = f.read()

print("File contents:\n", contents)
