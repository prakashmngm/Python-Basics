'''

Consider list of list : 
numList = 
[ [10,22,3], [4,15,6], [7,48,19] ]

-Print the element ‘15’

Add 4th element to every sublist such that the fourth element would be summation of first 3 elements.


'''

numList = [ [10,22,3], [4,15,6], [7,48,19] ]

print(numList[1][1])

for lst in numList:
    ele_sum = 0
    for ele in lst:
        ele_sum = ele + ele_sum
    lst.append(ele_sum)
#    lst.insert(len(lst),ele_sum)
print(numList)

