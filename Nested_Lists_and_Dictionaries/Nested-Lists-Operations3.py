'''

 Consider the foll. List of list : 
[ 
  [11, 5, 18, 628],
  [45, 87, 23, 1],
  [17, 23, 4, 90 ],
  [78, 311, 62, 9]
]

1) print the numbers positioned at odd position.

'''

num_list = [[11, 5, 18, 628],[45, 87, 23, 1],[17, 23, 4, 90 ],[78, 311, 62, 9]]
print(num_list[0][0],num_list[0][2])
print(num_list[1][0],num_list[1][2])
print(num_list[2][0],num_list[2][2])
print(num_list[3][0],num_list[3][2])

for lst_index in range(len(num_list)):
    for ele_index in range(len(num_list[lst_index])):
        if(ele_index % 2 == 0):
            print(num_list[lst_index][ele_index])

