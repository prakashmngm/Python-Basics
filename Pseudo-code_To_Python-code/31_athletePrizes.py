'''
Given input is list of scores of athletes for a sports game.
Scores by individual will be unique.

[5, 22, 45, 18, 36, 77]

Copy list = [0, 0, 0, 0, 0, 0]

Max = 5

max_Index = 0

Count = 7

Output list = [6 ,4,’Silver’,5,’Bronze’,’Gold’]

Index = 6

Pseudo code :
Take the input list ‘lst’
copy_list = lst
Output_list = []
Index = 0
In the loop : index < len(lst)
    output_list.append(0)
    index = index+1
Count = 1
In the loop : count <= len(lst)(6)
    Max = higestNumber(copy_list)
    Find the max_index of max in the copy_list
    Replace 0 at the max_index position in copy_list
    if(count == 1)
        Replace ‘Gold’ at the max_index position in the ouput_list
    elif(count == 2)
        Replace ‘Silver’ at the max_index position in the output_list
    elif(count == 3)
        Replace ‘Bronze’ at the max_index position in the output_list
    Else
        Replace count at the max_index position in the output_list
    Count = count+1
Return output_list
'''

def athletePrizes(lst):
    copy_list = lst
    output_list = []
    index = 0
    while(index < len(lst)):
        output_list.append(0)
        index = index+1
    count = 1
    while(count <= len(lst)):
        maximum = max(copy_list)
        max_index = copy_list.index(maximum)
        copy_list[max_index] = 0
        if(count == 1):
            output_list[max_index] = 'Gold'
        elif(count == 2):
            output_list[max_index] = 'Silver'
        elif(count == 3):
            output_list[max_index] = 'Bronze'
        else:
            output_list[max_index] = count
        count = count+1
    return output_list
    
print(athletePrizes([15]))
    
