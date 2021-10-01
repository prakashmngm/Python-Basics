'''

Given an array of integers, and given a value
Find any two numbers from array, whose summation is the given value.
Return list of indices of such two numbers.
Assume that solution always exist.


def summation(inputList, value ) : 

Sample Input1 :    [ 2,4,7,3,1 ]  , 10
Sample Output : [ 7, 3 ]

Sample Input2 :    [ -2,4,-6,-5,1 ]  , -2
Sample Output : [4,-6]

Sample Input3 :    [-2,4,-6,-4,1 ]  , 0
Sample Output : [4,-4]

In the loop : All the elements of the list(ele1)
    temp = val-ele1
    In the loop : All the elements of the list(ele2)
        if(ele2 == temp)
            return list(ele1,ele2)
'''

def summation(inputList, value ):
    for index1 in range(len(inputList)):
        temp = value-inputList[index1]
        for index2 in range(len(inputList)):
            if(inputList[index2] == temp):
                return list((index1,index2))
print(summation([ 2,4,7,3,1 ],10))


