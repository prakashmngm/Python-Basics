'''
Input array will have ‘n’ numbers in the range [0, n]
Find the missing number.



Input : [ 2,1,3,0,4 ]
Output : 5

Input : [0]
 Output : 1

Input : [0,1]
Output : 2

Input : [3,1,2]
Output : 0

Pseudo code:

Take the input list
length = len(list)
Create a dictionary with key as elements of the list with some dummy value ‘$’
Loop : Search for every element starting from 0 to length in the dictionary
    If the match doesn’t occur in the dictionary , return that value


'''

def findMissingNumber(lst):
    dictionary = {}
    for ele in lst:
        dictionary[ele] = '$'
    for element in range(len(lst)):
        if(element not in dictionary):
            return element
print(findMissingNumber([0,1,2,4,6,5]))
        
