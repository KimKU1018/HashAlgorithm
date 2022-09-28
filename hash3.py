hash_table = list([0 for i in range(8)])
#print(hash_table) # [0, 0, 0, 0, 0, 0, 0, 0]

def get_key(data):
    return hash(data)

get_key('seunghye') # 5687436291790947533

def hash_func(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_func(get_key(data))
    print(hash_address)
    print(hash_table[hash_address])



save_data('seunghye', '01043005555')
save_data('cy', '01045778844')

read_data('seunghye') # 2 # 01043005555
read_data('cy') # 0 # 01045778844

print(hash_table)