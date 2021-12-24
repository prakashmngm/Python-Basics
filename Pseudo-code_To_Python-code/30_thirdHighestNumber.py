'''
Given a list of numbers, find the 3rd highest distinct number.
If 3rd highest does not exist, then return the highest number.


11  12
0    1    2    3 
       ↑
big = 11
Index = 4
'''
'''
Take the input list of elements (lst)
highestNumber()
    big = lst[0]
    Index = 1
    In the loop : index < len(lst)(4)
        if( lst[index] > big)
            big = lst[index]
        index = index+1
    Return big
'''

def highestNumber(lst):
    big = lst[0]
    index = 1
    while(index < len(lst)):
        if(lst[index] > big):
            big = lst[index]
        index = index+1
    return big

'''
big = highestNumber(lst)
if( len(lst) > 1 )
    Remove all instances of big from the lst
Else
    Return big
'''
def thirdHighestNumber(lst):
    big = highestNumber(lst)
    if(len(lst) > 1):
        while(big in lst):
            lst.remove(big)
    else:
        return big
    '''
    if( len(lst) > 1 )
    big = highestNumber(lst)
    Else
        Return big
    if(len(lst) > 1 )
        Remove big from the lst
    Else
        Return big
    '''
    if(len(lst) > 1):
        big = highestNumber(lst)
    else:
        return big
    if(len(lst) > 1):
        while(big in lst):
            lst.remove(big)
    else:
        return big
    '''
    if( len(lst) > 1 )
        big = highestNumber(lst)
    elif(len(lst) == 1):
        return lst[0]
    else:
        Return big
    '''
    if(len(lst) > 1):
        big = highestNumber(lst)
        return big
    elif(len(lst) == 1):
        return lst[0]
    else:
        return big
    

print(thirdHighestNumber([-17,-2,-3]))
    



