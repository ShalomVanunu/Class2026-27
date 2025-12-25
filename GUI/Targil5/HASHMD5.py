import hashlib

def hash(data):
    hash_MD5 = hashlib.md5(data.encode()).hexdigest()
    return hash_MD5

