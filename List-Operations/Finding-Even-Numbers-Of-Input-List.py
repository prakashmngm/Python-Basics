'''

create a new list.
Each sublist consists of even numbers of the given sublists of the input list.

'''
even_list = []
for lst_index in range(len(num_list)):
    sub_list = []
    for ele_index in range(len(num_list[lst_index])):
        ele = num_list[lst_index][ele_index]
        if(ele % 2 == 0):
            sub_list.append(ele)
    even_list.append(sub_list)
print(even_list)


