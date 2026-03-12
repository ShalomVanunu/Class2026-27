import os
import shutil
import platform
from platform import system
import hashlib


def inf():
    data = os.popen("systeminfo").read()
    return data
   #  my_system = platform.uname()
 #print(f"Node Name: {my_system.node}")

def rhash(text):
 hash1 = hashlib.md5(text.encode()).hexdigest()
 return hash1

systemdata = inf()
comp_name = systemdata.split("\n")[1].split(":")[1].strip()
try :
    os.mkdir(comp_name)
except:
    pass
hash_systeminfo = rhash(inf())
os.chdir(comp_name)
with open(hash_systeminfo,"w") as file:
    file.write(inf())
#nameee="LABAI14"

#def totzaa():
# os.system("dir")
# output= os.popen("dir").read()
# name= str(os.system("HostName"))
# namee=os.popen("hostname").read().strip()

#def information():
# name3=platform.node()
# print(name3)





#def Main():
# print(platform.platform())
# information()
# totzaa()



 #if not os.path.exists(name3):
#os.chdir(r"{name3}")
#has= rhash(output)
#namehash=str(rhash(output)+"txt")
 #with open(namehash,"w") as file:
 # namehash.write(has)



Main()


