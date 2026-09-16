

FILE_NAME = "shalom.txt"

def read_file(filename):
    file_obj = open(filename, "r") # create object of file for reading "r"
    file_content = file_obj.readlines()
    print(file_content)



read_file(FILE_NAME)