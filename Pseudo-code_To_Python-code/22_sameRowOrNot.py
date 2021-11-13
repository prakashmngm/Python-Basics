'''
Problem Statement : 


If the input word consist of all characters from same row in the keyboard, print True.
Else print False.

Input : Alaska, Surya, asdf
Output : True, False, True

‘QWERTYUIOP’
‘ASDFGHJKL’
‘ZXCVBNM’

dict1 = {}
dict2 = {}
dict3 = {}

char = string[0]
	if(char in dict1):
		In the loop : from 2nd to last char of the string:
				if(char not in dict1):

					Return False
		Return True
		
		
	elif(char in dict2):
		In the loop : from 2nd to last char of the string:
				if(char not in dict2)
					Return False
		Return True
		
		
	Else:
		In the loop : from 2nd to last char of the string:
				if(char not in dict3)
					Return False
		Return True
'''

def sameRowOrNot(string):
    dict1 = {'Q':1,'W':1,'E':1,'R':1,'T':1,'Y':1,'U':1,'I':1,'O':1,'P':1}
    dict2 = {'A':1,'S':1,'D':1,'F':1,'G':1,'H':1,'J':1,'K':1,'L':1}
    dict3 = {'Z':1,'X':1,'C':1,'V':1,'B':1,'N':1,'M':1}
    char = string[0]
    index = 1
    if(char in dict1):
        while(index < len(string)):
            if(string[index] not in dict1):
                return False
            index = index+1
        return True
    elif(char in dict2):
        while(index < len(string)):
            if(string[index] not in dict2):
                return False
            index = index+1
        return True
    else:
        while(index < len(string)):
            if(string[index] not in dict3):
                return False
            index = index+1
        return True
print(sameRowOrNot('FALSE'))
