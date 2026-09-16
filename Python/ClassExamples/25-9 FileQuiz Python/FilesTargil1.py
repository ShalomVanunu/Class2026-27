

def are_files_equal(file1, file2):
    fileone=open(file1,"r")
    filetwo=open(file2, "r")
    if fileone.read()==filetwo.read():
        return True
    else:
        return False
file1=input("enter text")
file2=input("enter text")
print(are_files_equal(file1,file2))

