'''
Given an array of integers, find and delete duplicates.

Ex : [10,12,11,10,12] , [2,3,2,2,1,0]

{2 :[0,2,3], 3 : [1] ,1 : [4], 0:[5]}



    1. Take the input list
    2. dict = {}
    3. index = 0(1)
    4. length = len(lst)(1)
    5. In the loop : index < length
        1. if lst[index] does not exist in the dict
            1. Add lst[index] as the key to dict and create a list of index as value
        2. Else
            1. Go to the value of the key which is list of indices and append current index
        3. index = index+1

    6. In the loop dictionary:  Take the values of the dictionary 
        1. If len of list = 1, ignore
        2. If len of list > 1 : 
            Loop : the list starting from 2nd value : 
                    1. Use these indices and replace the index values with some dummy character in the original list
    7. Delete all the dummy characters in the original list to get the list without duplicate elements. 


'''

def remove_duplicates(lst):
    dict = {}
    index = 0
    length = len(lst)
    while(index < length):
        if(lst[index] not in dict):
            dict[lst[index]] = [index]
        else:
            dict[lst[index]].append(index)
        index = index+1
    for list_of_indices in dict.values():
        if(len(list_of_indices) == 1):
            continue
        else:
            for index1 in range(1,len(list_of_indices)):
                lst[index1] = '$'
    for ele in lst:
        if(ele == '$'):
            lst.remove('$')
    return lst

print(remove_duplicates([ 2,2,2,4,4,5,6,7,20,20]))
