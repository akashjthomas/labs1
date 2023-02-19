def combine_files(example1, file2):
    with open(example1, 'r') as f1, open(file2, 'r') as f2:
        # read the files line by line
        for line1, line2 in zip(f1, f2):
            print(line1.strip() + " " + line2.strip())

# test the function
combine_files("example1.txt", "file2.txt")
