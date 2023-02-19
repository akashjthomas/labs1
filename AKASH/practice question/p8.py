def find_longest_words(file2):
    with open(file2, 'r') as file:
        # read the file content
        text = file.read()
        # split the text into words
        words = text.split()
        # find the longest word
        longest_word = max(words, key=len)
        # find all words with the same length as the longest word
        longest_words = [word for word in words if len(word) == len(longest_word)]
        return longest_words

# test the function
print(find_longest_words("file2.txt"))
