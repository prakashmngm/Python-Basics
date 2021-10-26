'''
Problem Statement : 
Intersection concept of Set Theory.
Set1 = (1,2,3,4,5)
Set2 = ( 1,3,7,9)

Given two input lists, find their intersection list.

Eg : [3,5,2,7,11, 32]  [ 5, 9, 22, 43, 11]

[3,5, 2, 7,11, 32]
                ↑      

3 -> $
5 -> $
2 -> $
7 -> $
11 -> $
32 -> $
  
If (elem in dict): 
	output_list.append(elem)
[5, 9, 22, 43, 11] 
 ↑                                 
output_list = [5,11]

Take the input list1 and list2
dictionary = {}
output_list = []
if(len(list1) < len(list2)):
	Create a dictionary of list1
	for ele1 in list1:
		if(ele1 not in dictionary)
			dictionary[ele1] = ‘$’
	for ele2 in list2:
		if(ele2 in dictionary):
			output_list.append(ele2)
			del dictionary[ele2]
			
else:
	Create a dictionary of list2
	for ele2 in list2:
		if(ele2 not in list2)
			dictionary[ele2] = ‘$’
	for ele1 in list1:
            if(ele1 in dictionary):
                output_list.append(ele1)
                del dictionary[ele1]
return output_list

'''

def intersection(list1,list2):
    dictionary = {}
    output_list = []
    if(len(list1) <= len(list2)):
        for ele1 in list1:
            if(ele1 not in dictionary):
                dictionary[ele1] = '$'
        for ele2 in list2:
            if(ele2 in dictionary):
                output_list.append(ele2)
                del dictionary[ele2]
    else:
        for ele2 in list2:
            if(ele2 not in dictionary):
                dictionary[ele2] = '$'
        for ele1 in list1:
            if(ele1 in dictionary):
                output_list.append(ele1)
                del dictionary[ele1]
    return output_list

print(intersection([1,2,3,4,5],[1,3,7,9]))
