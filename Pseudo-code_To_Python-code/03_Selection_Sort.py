'''
>Selection Sort

List of integers -> 3, 1, 5, 2, 6, 4

                         -> 3, 1, 5, 2, 4 | 6
 
                         -> 3, 1, 4, 2, | 5, 6

Take the input as list of input integers[3, 1, 5, 2, 6, 4]
length = len(lst)
In the loop : length > 0
    index = 0
    max_index = index
    max_value = lst[index]
    In the loop : index < length
        if(max_value < lst[index])
    	    max_value = lst[index]
    	    max_index = index
        index = index+1
    swap(lst[max_index],lst[length-1]):
    	temp = lst[max_index]
    	lst[max_index] = lst[length-1]
    	lst[length-1] = temp
    length = length -1
print(lst)

'''

def Selection_Sort(lst):
    length = len(lst)
    while(length > 0):
        index = 0
        max_index = index
        max_value = lst[index]
        while(index < length):
            if(max_value < lst[index]):
                max_value = lst[index]
                max_index = index
            index = index+1
        temp = lst[max_index]
        lst[max_index] = lst[length-1]
        lst[length-1] = temp
        length = length-1
    return lst
    
print(Selection_Sort([-1 , -5 , -3 , 8 , 2 , 7 , 1]))
        
