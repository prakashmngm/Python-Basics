'''
Given two sorted lists. Merge both of them to create a new sorted list.

def mergeSortedList( list1, list2 ) : 

Eg : [2,3,5,7]  [ 2,5,9 ]
Output : [ 2, 2, 3, 5, 5, 7, 9]

arr1 = 0
arr2 = 0
Initialize an empty list3

'''

def mergeSortedList(list1,list2):
    index1 = 0
    index2 = 0
    len1 = len(list1)
    len2 = len(list2)
    list3 = []
    '''
    Loop : arr1 < end of list1  AND arr2 < end of list2
    if( arr1 <= arr 2 )
    append arr1 to list3
    Arr1 moves one pos ahead
    else 
    append arr2 to list3
    Arr2 moves one pos ahead
    
    '''
    
    while(index1 < len1 and index2 < len2):
        if(list1[index1] <= list2[index2]):
            list3.append(list1[index1])
            index1 = index1+1
        else:
            list3.append(list2[index2])
            index2 = index2+1
    '''
    if( arr1 < end of list1 )
	Copy all list1 elements from arr1 to list3
	
    '''
    if(index1 < len1):
        for index in range(index1,len1):
            list3.append(list1[index])
    '''
    if( arr2 < end of list2 )
	Copy all list2 elements from arr2 to list3
    return list3
    
    '''
    if(index2 < len2):
        for index in range(index2,len2):
            list3.append(list2[index])
    return list3
    
print(mergeSortedList([2,2,2,2],[2,2,2,2]))



