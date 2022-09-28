hash_table = [0 for i in range(10)]

def hash_func(key):
    hashValue=ord(key)
    hashAdress = hashValue%10
    return hashAdress

def save_data(key, value):
    idx = hash_func(key)
    hash_table[idx]=value
def read_data(key):
    idx = hash_func(key)
    return hash_table[idx]