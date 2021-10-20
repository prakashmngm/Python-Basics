'''
Pascal’s Triangle

                  1
               1    1
            1    2    1
         1     3     3   1
      1    4     6     4   1

Input : <Row Number of the Pyramid> 3 
Output : [ [1] , [1, 1] , [1, 2, 1] ]

row_num = 5

main_list = [[1] , [1,1], [1,2,1],[1,3,3,1],[1,4,6,4,1]]                                                       ↑
index = 3
length = 3
temp_list =  [1,4,6,4,1]
summ = 4

Pseudo Code:

Take the input row_num(5)
if(row_num == 1)
	main_list = [[1]]
	return main_list
elif(row_num == 2)
	main_list = [[1] , [1,1]]
	return main_list
else
	main_list = [[1] , [1,1]]
	In the loop : row_num > len(main_list)
index = 0
last_list_index = len(main_list)-1
length = len(main_list[last_list_index])-1
temp_list = [1]
		In the loop : index < length
				 summ = 0
				 summ = main_list[last_list_index][index]+main_list[last_list_index][index+1]
				 temp_list.append(summ)
				 index = index+1
		temp_list.append(1)
		main_list.append(temp_list)

	return main_list

'''
def Pascal_Triangle(row_num):
    if(row_num == 1):
        main_list = [[1]]
        return main_list
    elif(row_num == 2):
        main_list = [[1],[1,1]]
        return main_list
    else:
        main_list = [[1],[1,1]]
        while(row_num > len(main_list)):
            index = 0
            last_list_index = len(main_list)-1
            length = len(main_list[last_list_index])-1
            temp_list = [1]
            while(index < length):
                summ = 0
                summ = main_list[last_list_index][index]+main_list[last_list_index][index+1]
                temp_list.append(summ)
                index = index+1
            temp_list.append(1)
            main_list.append(temp_list)
        return main_list
print(Pascal_Triangle(25))
