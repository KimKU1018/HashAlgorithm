hash_table = [0 for i in range(8)]

def hash_func(data):
    return hash(data) % 8

def set_data(data, value):
    key = hash_func(data)
    hash_table[key] = value

def get_data(data):
    key = hash_func(data)
    return hash_table[key]