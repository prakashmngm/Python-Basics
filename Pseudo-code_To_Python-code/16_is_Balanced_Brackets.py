'''
Given a string of brackets, identify if they are balanced.
Valid Inputs :
       
 (())()
  ↑
(())()

Pseudo Code:
Take the input string of brackets.
Index = 0
if(string[index] == ‘)’)
    Return false
if( (len(string)%2) == 1)
    Return false
stack = []
In the loop : index < len(string) (2)
            if( string[index] == ‘(‘ )
                stack.append(string[index])
            else
                if(len(stack) == 0)
                    Return false
                stack.pop()
            index = index+1
if(len(stack) == 0)
    Return true
else
    Return false

'''

def is_Balanced_Brackets(string):
    index = 0
    if(string[index] == ')'):
        return False
    if(len(string)%2 == 1):
        return False
    stack = []
    while(index < len(string)):
        if(string[index] == '('):
            stack.append('(')
        else:
            if(len(stack) == 0):
                return False
            stack.pop()
        index = index+1
    if(len(stack) == 0):
        return True
    else:
        return False

print(is_Balanced_Brackets('(())()'))

