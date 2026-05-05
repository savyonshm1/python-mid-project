import os


# question 2
def get_file_size(filename:str):
    try:
        open(filename)
    # if the file doesn't exist
    except FileNotFoundError:
        return -1  # file size can't be a negative number, so this value is an indicator
                   # for the code that will use this function
    # if the file exists - return file size (in bytes)
    return os.path.getsize(filename)


# question 3
def validate_string_format(string:str):
    # if it's shorter than 9 chars - necessarily doesn't match the pattern
    if len(string) < 9:
        return False
    # if the first 3 chars are not uppercase letters - doesn't match the pattern
    if not string[0:3].isupper():
        return False
    # if the next 4 chars are not digits - doesn't match the pattern
    if not string[3:7].isdigit():
        return False
    # if the next 2 chars are not lowercase letters - doesn't match the pattern
    if not (string[7:9].islower() and string[7:9].isalpha()):
        return False
    # if the code reached here - all the previous conditions are true, and the string matches the pattern
    return True


# question 4
def get_sum_size(files_list:list):
    # if the list is empty - the sum is 0
    if len(files_list) == 0:
        return 0
    sum = 0
    # go through every item in the list
    for file in files_list:
        size = get_file_size(file)
        # if the file exists (the function returns -1 if not)
        if size != -1:
            sum += size
    return sum


# question 5
def get_words_from_file(filename:str):
    # check if the file exists
    try:
        file = open(filename, 'r')
    # if the file doesn't exist
    except FileNotFoundError:
        # returns None so the code that will use this func knows it means the file doesn't exist
        return None

    # create a list that contains all the words in the file (without \n-s), each word as a different item
    words = file.read().replace('\n',' ').split(' ')
    # convert to set to get all unique words without duplicates
    return list(set(words))


# question 9
def add_word_if_not_exist(filename:str, word:str):
    try:
        file = open(filename, 'r+')  # when using r+ the cursor stays at the beginning of the file
    # if the file doesn't exist, a new file won't be created
    except FileNotFoundError:
        return
    # if there is another problem with the file
    except OSError:
        return
    # if the input is not a string - won't add it to the file
    if type(word) != str:
        return
    content = file.read()
    # searches through a list of the words of the file
    if word not in content.replace('\n', ' ').split(' '): # moves the cursor to the end of file
        # add a space so the word won't connect the word to the previous word (for future runs of the function)
        file.write(' ' + word)

