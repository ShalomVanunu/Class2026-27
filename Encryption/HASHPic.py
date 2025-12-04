import hashlib

with open("Dog_Breeds.jpg", "rb") as file:
    data_file = file.read()

hash_MD5 = hashlib.md5(data_file).hexdigest()

with open("Dog_Breeds1.jpg", "rb") as file:
    data_file1 = file.read()

hash_MD5_1 = hashlib.md5(data_file1).hexdigest()

print("MD5 Hash Original" ,hash_MD5)
print("MD5 Hash Changed" ,hash_MD5_1)