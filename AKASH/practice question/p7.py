def write_list_to_file(list, data_list):
    with open(list, 'w') as file:
        # write each item in the list to a new line
        for item in data_list:
            file.write(str(item) + '\n')

# test the function
data = ['item1', 'item2', 'item3']
write_list_to_file('example2.txt', data)
