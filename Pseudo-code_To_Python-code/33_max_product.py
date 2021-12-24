'''
Given a list of integers(except zero), find the maximum product of three numbers.

Neg_count = 2
Pos_count = 1
Pos_product = 
Neg_product = 
Pseudo Code :
[200, -50, 5, 7, -3, 100]
Sort the input list : [ -50, -3, 5, 7, 100, 200]

1.Find Negitive_count, Positive_count
-Sort the input list. Find the first positive number.
-Negative count = Index of 1st Positive Number.
-Positive Count = Len(list) - Index of 1st Positive Number 
'''
def max_product(lst):
    if(len(lst) <= 3):
        product = 1
        for ele in lst:
            product = product*ele
        return product
    lst.sort()
    print(lst)
    index = 0
    while(index < len(lst)):
        if(lst[index] > 0):
            break
        index = index+1
    neg_count = index
    pos_count = len(lst)-index
    print(neg_count,pos_count)
    
    '''
    2. If Negitive_Count = 0
    	All are positive numbers
    	Find 1st_max , 2nd_max , 3rd_max
    	Answer is product of above 3 numbers.
    '''
    if(neg_count == 0):
        return (lst[-1]*lst[-2]*lst[-3])
    '''
    3. If Positive_count = 0
    	All are Negitive Numbers
    	Find 1st_max , 2nd_max , 3rd_max
    	Answer is product of above 3 numbers
    '''
    if(pos_count == 0):
        return (lst[-1]*lst[-2]*lst[-3])

    '''
    4 . /* since we are here, we have list with both neg & pos numbers */
    	Create 2 sep lists, Pos_Numbers & Neg_Numbers  
             -Find 1st max from Pos_Numbers. 
    	
            -Initialize Positive_product = 0. 
             if( len of Pos_Numbers >= 3 )  
                  2nd , 3rd max from Pos_numbers. Take their product.(15)
    '''
    positive_list = []
    negitive_list = []
    seperator = index
    while(index < len(lst)):
        positive_list.append(lst[index])
        index = index+1
    start = 0
    while(start < seperator):
        negitive_list.append(lst[start])
        start = start+1
    print(positive_list,negitive_list)
    first_max = positive_list[-1]
    print(first_max)
    pos_product = 0
    if(len(positive_list) >= 3):
        pos_product = (positive_list[-2]*positive_list[-3])
    print(pos_product)
    
    '''
           -Initialize Neg_Product = 0
            if( len of Neg_Numbers >= 2 ) 
           Find 1st & 2nd min from Neg_Numbers. Take their product.()
    
          - Compare their products. 
    If (neg product > pos_prodcut), return (1st max of positive * Neg_Product) 
    Else return (1st max of positive * Pos_Product) 
    '''
    neg_product = 0
    if(len(negitive_list) >= 2):
        neg_product = negitive_list[0]*negitive_list[1]
    if(neg_product > pos_product):
        return first_max*neg_product
    else:
        return first_max*pos_product
        
print(max_product([10, -2, 5,-4,2,1,3,6,-4,-3,-6]))
