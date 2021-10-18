'''
[]
         ↑
[]
         ⇑

[9,9,9,9,0]

index1 = -1
index2 = -1
summ = 9
carry = 0
digit = 0


index1 =  len(list1)-1
index2 = len(list2)-1
carry = 0
list3 = []
In the loop : index1 >= 0 and index2 >= 0
                summ = list1[index1]+list2[index2]+carry
                if(summ < 10)
                	Pre append list3 with summ
                	index1 = index1-1
                	Index2 = index2-1
                	carry = 0
                else
                	digit = summ%10
                	Pre append list3 with digit
                	index1 = index1-1 
                	Index2 = index2-1
                	carry = 1
	
'''
def addition_of_two_numbers(list1,list2):
    index1 = len(list1)-1
    index2 = len(list2)-1
    carry = 0
    list3 = []
    while(index1 >= 0 and index2 >= 0):
        summ = list1[index1]+list2[index2]+carry
        if(summ < 10):
            list3.insert(0,summ)
            index1 = index1-1
            index2 = index2-1
            carry = 0
        else:
            digit = summ%10
            list3.insert(0,digit)
            index1 = index1-1
            index2 = index2-1
            carry = 1
        if(index1 < 0 and index2 < 0 and carry == 1):
            list3.insert(0,carry)
    print(list3)
        
    '''
    In the loop : (index1 >= 0 )
    	if(carry == 1):
    		summ = list1[index1] + carry
    		if(summ < 10)
    			Pre append summ to list3
    			Index1 = index1-1
       			carry = 0
    			In the loop : index1 >= 0
    					Pre append each element of list1 from index1 position
    					Index1 = index1-1
    		else
    			digit = summ%10
    			Pre append list3 with digit
    			Index1 = index1-1
    			carry = 1
    	else:
    		In the loop : index1 >= 0
    				Pre append each element of list1 from index1 
    				Index1 = index1-1
    	if(index1 < 0 and carry == 1)
    		Pre append carry to list3
    '''
    while(index1 >= 0):
        if(carry == 1):
            summ = list1[index1]+carry
            if(summ < 10):
                list3.insert(0,summ)
                index1 = index1-1
                carry = 0
                while(index1 >= 0):
                    list3.insert(0,list1[index1])
                    index1 = index1-1
            else:
                digit = summ%10
                list3.insert(0,digit)
                index1 = index1-1
                carry = 1
        else:
            while(index1 >= 0):
                list3.insert(0,list1[index1])
                index1 = index1-1
        if(index1 < 0 and carry == 1):
            list3.insert(0,carry)
    print(list3)
            
    '''
    In the loop :(index2 >= 0)
    	lf(carry == 1)
    		summ = list2[index2] + carry
    		if(summ < 10)
    			Pre append summ to list3
    			Index2 = index2-1
    			carry = 0
    			In the loop : index2 >= 0
    					Pre append all elements of list2 from index2
    					Index2 = index2-1
    
    
    		else
    			digit = summ%10
    			Pre append list3 with digit
    			Index2 = index2-1
    			carry = 1
    	else:
    		In the loop : index2 >= 0
    				Pre append each element of list2 from index2 
    				Index2 = index2-1

    	if(index2 < 0 and carry == 1)
    		Pre append carry to list3
    
    return list3
    
    '''
    while(index2 >= 0):
        if(carry ==1):
            summ = list2[index2]+carry
            if(summ < 10):
                list3.insert(0,summ)
                index2 = index2-1
                carry = 0
                while(index2 >= 0):
                    list3.insert(0,list2[index2])
                    index2 = index2-1
            else:
                digit = summ%10
                list3.insert(0,digit)
                index2 = index2-1
                carry = 1
        else:
            while(index2 >= 0):
                list3.insert(0,list2[index2])
                index2 = index2-1
        if(index2 < 0 and carry == 1):
            list3.insert(0,carry)  
    return list3
            
print(addition_of_two_numbers([9,9],[9,9]))


