hash_table = list([None for i in range(16)])

def hash_function(key):
    return key % 16