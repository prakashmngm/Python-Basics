'''
Problem Statement : 
Pattern = “abab”
Input String = “dog cat dog dog”

aab
dog dog dog
If input string follows input pattern, return True.
Else return false.

'''

def patternComparision(pattern,string):
    '''
    Create a dictionary for the input pattern , key as the character and value as the list of indices of the character in the input pattern
    '''
    
    dict1 = {}
    for index in range(len(pattern)):
        if(pattern[index] not in dict1):
            list_of_indices = []
            list_of_indices.append(index)
            dict1[pattern[index]] = list_of_indices
        else:
            dict1[pattern[index]].append(index)
    '''
    Split the given input string into list of elements based on the space
    '''
    
    lst = string.split(' ')
    
    '''
    Create another dictionary , key as the element of the list and value as the indices of the element
    '''
    
    dict2 = {}
    for index in range(len(lst)):
        if(lst[index] not in dict2):
            list_of_indices = []
            list_of_indices.append(index)
            dict2[lst[index]] = list_of_indices
        else:
            dict2[lst[index]].append(index)
    
    '''
    if(len(dict1) != len(dict2) )
	    Return false
	'''
    if(len(dict1) != len(dict2)):
        return False
    '''
    list1 = dict1.values()
    list2 = dict2.values()

    Index = 0
    In the loop : index < len(list1)
    	if (list1[index] != list2[index2])
    		Return false
    	Index = index+1
    Return true
    
    '''
    
    list1 = list(dict1.values())
    list2 = list(dict2.values())
    index = 0
    while(index < len(list1)):
        if(list1[index] != list2[index]):
            return False
        index = index+1
    return True

print(patternComparision('aa','mo mo na'))
