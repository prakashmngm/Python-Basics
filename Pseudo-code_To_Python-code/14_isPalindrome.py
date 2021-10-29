'''
Input : A string of characters. Determine if it is a palindrome.

Ex : ‘  ’
                  ↑
Length = 2
Stopper = 1
Index = 1

Pseudo Code :
Take the input string
length = len(string)
stopper = length/2
index = 0
In the loop: index < stopper
    if(string[index] != string[length-(index+1)])
        return false
    Index = index+1
Return true
'''

def isPalindrome(string):
    length = len(string)
    stopper = length/2
    index = 0
    while(index < stopper):
        if(string[index] != string[length-(index+1)]):
            return False
        index = index+1
    return True

print(isPalindrome('10101'))
