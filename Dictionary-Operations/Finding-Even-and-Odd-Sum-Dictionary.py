'''

 Consider the foll. List of list : 
[ 
  [11, 5, 18, 628],
  [45, 87, 23, 1],
  [17, 23, 4, 90 ],
  [78, 311, 62, 9]
]

{ 1 : [ even_sum, odd_sum], 
2 : [ , ],
3 : [ , ], 
4 : [ , ]
}

Find out the list of even numbers from the sublists of given list
Find out the list of odd numbers from the sublists of given list
Prepare a final even_sum list
Prepare a final odd_sum list
Prepare a final even_odd_sum list
Prepare a dictionary from the even_odd_sum list


'''

num_list = [[11, 5, 18, 628],[45, 87, 23, 1],[17, 23, 4, 90 ],[78, 311, 62, 9]]

even_list = []
odd_list = []
for lst_index in range(len(num_list)):
    even_sub_list = []
    odd_sub_list = []
    for ele_index in range(len(num_list[lst_index])):
        ele = num_list[lst_index][ele_index]
        if(ele % 2 == 0):
            even_sub_list.append(ele)
        else:
            odd_sub_list.append(ele)
    even_list.append(even_sub_list)
    odd_list.append(odd_sub_list)
print(even_list)
print(odd_list)

even_sum_list = []
for list_index in range(len(even_list)):
    even_sum = 0
    for ele_index in range(len(even_list[list_index])):
        even_sum = even_sum + even_list[list_index][ele_index]
    even_sum_list.append(even_sum)
print(even_sum_list)

odd_sum_list = []
for list_index in range(len(odd_list)):
    odd_sum = 0
    for ele_index in range(len(odd_list[list_index])):
        odd_sum = odd_sum + odd_list[list_index][ele_index]
    odd_sum_list.append(odd_sum)
print(odd_sum_list)

even_odd_sum_list = []
for index in range(len(even_sum_list)):
    sub_list = []
    sub_list.append(even_sum_list[index])
    sub_list.append(odd_sum_list[index])
    even_odd_sum_list.append(sub_list)
print(even_odd_sum_list)

even_odd_sum_dict = {}
for index in range(len(even_odd_sum_list)):
    even_odd_sum_dict[index+1] = even_odd_sum_list[index]
print(even_odd_sum_dict)

