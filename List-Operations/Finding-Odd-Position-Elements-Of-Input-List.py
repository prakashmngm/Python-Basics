'''
create a new list.
Each sublist consists of odd position elements of the given input list.

'''

new_list = []

for lst_index in range(len(num_list)):
    sub_list = []
    for ele_index in range(len(num_list[lst_index])):
        if(ele_index % 2 == 0):
            sub_list.append(num_list[lst_index][ele_index])
    new_list.append(sub_list)
print(new_list)

