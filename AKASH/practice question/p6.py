def copy_file(example1, copy):
    with open(example1, 'r') as file:
        # read the file content
        text = file.read()
    with open(copy, 'w') as new_file:
        # write the content to the new file
        new_file.write(text)

# test the function
copy_file("example1.txt", "copy.txt")
