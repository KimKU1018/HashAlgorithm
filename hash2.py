#list comprehension
#위 코드의 출력표현식을 i에서 i*i로 바꾼 결과


hash_table = list([i*i for i in range(10)])
print(hash_table)

#dataset = [False, 49, "seunghye", 31.43, 6, 10]
#int_data = [num for num in dataset if type(num)==int]
#print(int_data) # [49, 6, 10]

dataset = [False, 49, "seunghye", 31.43, 6, 10]
int_data = [num for num in dataset if type(num)==int]
print(int_data)