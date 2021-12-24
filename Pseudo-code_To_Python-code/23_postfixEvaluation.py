'''
Problem Statement : Evaluate Reverse Polish Notation using Stack.

Solve -> 6 12 3 8 + - * 

[6,12,3,8,'+','-','*']

Pseudo Code:

Take the input list of characters
Index = 0
In the loop : index < len(string)
        Char = string[index]
        Check if the character is operand or operator
            If (char is not operator):
                Push on to the stack
            Else
                Pop two items from the stack
                Apply the operator to the popped items from the stack
                Push the result on to the stack
        Index = index+1
Result = stack.pop()
Return the result
'''

def postfixEvaluation(lst):
    '''
    Take the input list of characters
    Index = 0
    '''
    index = 0
    stack = []
    while(index < len(lst)):
        '''
        Char = string[index]
        Check if the character is operand or operator
        If (char is not operator):
                Push on to the stack
        Else
            Pop two items from the stack
            Apply the operator to the popped items from the stack
            Push the result on to the stack
        Index = index+1
        '''
        char = lst[index]
        if(char not in ('+','-','*','/')):
            stack.append(char)
        else:
            temp2 = stack.pop()
            temp1 = stack.pop()
            if(char == '+'):
                result = temp1+temp2
            elif(char == '-'):
                result = temp1-temp2
            elif(char == '*'):
                result = temp1*temp2
            else:
                result = temp1/temp2
            stack.append(result)
        index = index+1
    '''
    Result = stack.pop()
    Return the result
    '''
    result = stack.pop()
    return result

print(postfixEvaluation([10,2,8,'*','+',3,'-']))

