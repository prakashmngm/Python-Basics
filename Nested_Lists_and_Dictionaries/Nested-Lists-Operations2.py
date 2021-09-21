'''
create a new list of 3 sublists .
Each sublist will consists of 4 elements.
Each element of the sublist is square of original element.

print every sublist of given list in one line.

print the square of every element of the list

'''
new_list = [[],[],[]]
index = 0
for lst in numList:
    for ele in lst:
        new_list[index].append(ele*ele)
    index = index+1
print(new_list)

