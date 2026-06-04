# Write A Python Program To Get File Name From User Without Space
file_name = input("Enter file name: ")

if " " in file_name:
    print("File name should not contain spaces.")
else:
    print("Valid file name:", file_name)