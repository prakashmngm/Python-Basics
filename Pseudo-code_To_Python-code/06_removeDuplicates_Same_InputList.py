'''
Given an array of integers, sorted in ascending order.
Find and delete duplicates, if any.

def removeDuplicates(inputList) : 

Sample Input : [2,2,2,4,4,5,6,7,20,20]
Sample Output : [ 2,4,5,6,7,20 ]

InputList : [2,2,2,4,4,5,6,7,20,20]
            [2,2,4,4,5,6,7,20,20]
            [2,4,4,5,6,7,20,20]
            [2,4,5,6,7,20,20]
            [2,4,5,6,7,20]

if(len(inputList) == 0 or  len(inputList) == 1)
	return inputList
	length = len(inputList)
	arry_index = 0
In the loop : index = 0 to (length-2)
	if(inputList[arry_index] == inputList[arry_index+1])
		remove inputList[arry_index]
	else
	    array_index = array_index+1
	index = index+1
return inputList

'''

# Removing Duplicates in the given InputList

def removeDuplicates(inputList):
    if(len(inputList) == 0 or  len(inputList) == 1):
        return inputList
    iterator = 0
    index = 0
    length = len(inputList)
    while(iterator <= (length-2)):
        if(inputList[index] == inputList[index+1]):
	        inputList.pop(index)
        else:
	        index = index+1
        iterator = iterator+1
    return inputList
    
print(removeDuplicates([ 2,3,4,5 ]))
	       
	    

