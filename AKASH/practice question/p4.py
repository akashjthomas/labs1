def is_file_closed(file_object):
    try:
        file_object.read()
    except ValueError:
        return True
    return False

# test the function
file = open("example1.txt", "r")
print(is_file_closed(file)) # will return False
file.close()
print(is_file_closed(file)) # will return True
