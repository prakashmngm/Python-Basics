'''
Given an array of integers, sorted in ascending order.
Find and delete duplicates, if any.

def removeDuplicates(inputList) : 

Sample Input : [ 2,3,4,5 ]
Sample Output : [ 2,3,4,5 ]

Sample Input : [2,2,2,4,4,5,6,7,20,20]
Sample Output : [ 2,4,5,6,7,20 ]

Sample Input : [-4 , -4 , -2 , -2 , -1]
Sample Output : [-4,-2,-1]

Sample Input : [0,0,0,1,2,3]
Sample Output : [0,1,2,3]

Sample Input : []
Sample Output : []

Sample Input : [-3]
Sample Output : [-3]

if(len(inputList) Greater than 1)
    outputList = inputList[0]
    In the loop: All elements in the inputList from 2nd to last element
        if(ele Not Equals last_ele of outputList)
            insert the last_ele into outputList
return outputList

'''

# Using Extra Array outputList for the computation

def removeDuplicates(inputList):
    if(len(inputList) > 1):
        outputList = []
        outputList.append(inputList[0])
        for index in range(1,len(inputList)):
            if(inputList[index] != outputList[-1]):
                outputList.append(inputList[index])
        return outputList
    else:
        return inputList

print(removeDuplicates([ 2,3,4,5 ]))
