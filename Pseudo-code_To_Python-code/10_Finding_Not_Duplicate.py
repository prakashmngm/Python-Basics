'''
Given a list of integers, all of them have duplicates, except one.
List will not be empty.
Find that number.

Input : [ 2, 3, 4, 4, 3, 2, 5, 6, 7,  7, 6 ]

2 →2
3→2
4→2
5→1
6 →2
7→2

Take the input list
dict_count = {}
In the loop : for each element(ele) of the list
                If the element does not exist as key
                    dict_count[ele] = 1
                If the element already exists as key
                    dict_count[ele] = dict_count[ele]+1
In the loop : for each key,value in dict_count.items()
                if (value == 1):
                Return the corresponding key


'''
def Finding_Not_Duplicate(lst):
    dict_count = {}
    for ele in lst:
        if(ele not in dict_count):
            dict_count[ele] = 1
        else:
            dict_count[ele] = dict_count[ele]+1
    for key,value in dict_count.items():
        if(value == 1):
            return key
print(Finding_Not_Duplicate([2, 3, 4, 5, 3, 2, 5, 6, 7,  7, 6]))
             
             
        
