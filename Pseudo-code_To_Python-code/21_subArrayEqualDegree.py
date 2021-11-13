'''
Input array = [ 6, 3, 3, 5, 8, 8, 5, 8…..8……..8... ]
Find the degree of the array = max. Frequency of any element in the array.

In the output, print the sub-array from the main array, such that 
a)the sub-array has same degree as main array 

b) it has the smallest possible length.

-1 -> 1
-2 -> 1
-3 -> 1
-4 -> 1
-5 -> 1

[4 -7]

Input array = [-1,-3,-2,-5,-4]

[-1,-3,-2,-5,-4]

Output array = [2,5,7,6,3]

[0,0],[1,1],[2,2],[3,3],[4,4]

[-1] , [-3], [-2],[-5],[-4]
[-1]

Take the input array
'''

def subArrayEqualDegree(lst):
    '''
    Create a dictionary with key as element and value as the count of the element
    '''
    dictionary = {}
    for ele in lst:
        if(ele not in dictionary):
            dictionary[ele] = 1
        else:
            dictionary[ele] = dictionary[ele]+1
    '''
    Find the list of the keys which have the maximum count
    '''
    max_val = max(dictionary.values())
    max_key_list = []
    for key,value in dictionary.items():
        if(value == max_val):
            max_key_list.append(key)
    print(max_key_list)
    '''
    Search for every max_key in the input array from the starting and find the start-index
    Search for every max_key in the input array from the ending and find the end-index
    
    -1 -> 1
    -2 -> 1
    -3 -> 2
    -4 -> 1
    -5 -> 2
    max_key_list = [1,2,3,4]
    lst = [1,2,3,4]
    start_end_index_list = []
    start_index = 0
    end_index = 0
    last_index = 0
    start_end_index_list = [[0,0]]
    sub_array_length_list = [4,4]
    '''
    start_index = 0
    end_index = 0
    start_end_index_list = []
    for key in max_key_list:
        for index in range(len(lst)):
            if(key == lst[index]):
                start_index = index
                break
        last_index = len(lst)-1
        while(last_index >= 0):
            if(key == lst[last_index]):
                end_index = last_index
                break
            last_index = last_index-1
        print(end_index)
        start_end_index_list.append(list((start_index,end_index)))
    print(start_end_index_list)
    '''
    Create a list for start-index and end-index for every key
    Create a new sub array from the input array from start-index position to end-index position for every [start-index,end-index]
    Find the shortest length sub array 
    '''
    sub_array_length_list = []
    for sub_list in start_end_index_list:
        length = (sub_list[1]-sub_list[0])+1
        sub_array_length_list.append(length)
    min_length = sub_array_length_list[0]
    for length in sub_array_length_list:
        if(length < min_length):
            min_length = length
    sub_arrary_index = sub_array_length_list.index(min_length)
    index_list = start_end_index_list[sub_arrary_index]
    start_index = index_list[0]
    end_index = index_list[1]
    sub_array = []
    print(start_index,end_index)
    print(lst)
    while(start_index <= end_index):
        sub_array.append(lst[start_index])
        start_index = start_index+1
    return sub_array
    
print(subArrayEqualDegree(['ra','ma','ki','ma','ra','ki']))
