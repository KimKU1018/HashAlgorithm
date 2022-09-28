hash = dict()
hash = {}

hash[1] = 'apple'
hash['banana'] = 3
hash[(4, 5)] = [1,2,3]
hash[10] = dict({1:'a', 2:'b'})

hash.pop(1) #apple이 삭제됨
del hash[1]
hash.pop('banana') # 3이 삭제됨
del hash['banana']
hash.pop((4,5)) #[1, 2, 3]이 삭제됨
del hash[(4,5)]

hash.keys()
hash.values()
hash.items()