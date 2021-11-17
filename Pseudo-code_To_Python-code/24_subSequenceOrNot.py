'''

Given two input strings : 
Big : abcdef, Small : ace

Return true if ‘small’ is subsequence of ‘Big’
Subsequence : By deleting zero or more characters from the Big string.


Big : ‘’
        ↑
Small : ‘’
            ↑
Big-index = 0
Small-index = 0
Char = 

Pseudo Code:
Take the two input strings (Big,Small)
big-index = 0
small-index = 0
In the loop : big-index < len(big) and small-index < len(small)
        char = small[small-index]
        if(char == big[big-index])
            big-index = big-index+1
            small-index = small-index+1
        Else:
            big-index = big-index+1
if(big-index == len(big) and small-index != len(small))
    Return False
Else:
    Return True

'''

def subSequenceOrNot(big,small):
    '''
    Take the two input strings (Big,Small)
    big-index = 0
    small-index = 0
    In the loop : big-index < len(big) and small-index < len(small)
            char = small[small-index]
            if(char == big[big-index])
                big-index = big-index+1
                small-index = small-index+1
            Else:
                big-index = big-index+1
    '''
    big_index = 0
    small_index = 0
    while(big_index <len(big) and small_index < len(small)):
        char = small[small_index]
        if(char == big[big_index]):
            big_index = big_index+1
            small_index = small_index+1
        else:
            big_index = big_index+1
    '''
    if(big-index == len(big) and small-index != len(small))
        Return False
    else:
        Return True
    '''
    if(big_index == len(big) and small_index != len(small)):
        return False
    else:
        return True

print(subSequenceOrNot('','123'))

