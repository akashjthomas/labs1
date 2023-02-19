def remove_newlines(example1):
    with open(example1, 'r') as file:
        # read the file content
        text = file.read()
        # replace newline characters with empty string
        text = text.replace('\n', '')
    with open(example1, 'w') as file:
        # write the modified text back to the file
        file.write(text)

# test the function
remove_newlines("example1.txt")
