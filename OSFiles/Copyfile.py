import shutil
import os

current_directory = os.getcwd()
dest_dir = current_directory+"\\ShalomV"
shutil.copy("Hello.txt", dest_dir)
os.remove("Hello.txt")
