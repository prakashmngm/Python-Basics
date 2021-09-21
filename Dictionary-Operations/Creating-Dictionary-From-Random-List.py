'''
Creating a dictionary from a random list

'''

lst = [2,1,3,6,3]
dict_lst = {}
for index in range(len(lst)):
    dict_lst[index+1] = lst[index]
print(dict_lst)

