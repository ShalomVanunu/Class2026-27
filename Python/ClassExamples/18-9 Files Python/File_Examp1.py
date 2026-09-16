

FILE_NAME = "STORY.TXT"

def read_file(filename):
    file_obj = open(filename, "r") # create object of file for reading "r"
    file_content = file_obj.read()
    word_to_search = input("Enter a word to search: ")
    if word_to_search in file_content:
        print("the word is in the text file")

    #for word in file_content.split():







read_file(FILE_NAME)