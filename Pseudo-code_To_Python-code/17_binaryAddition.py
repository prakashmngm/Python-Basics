'''
Eg : “10101”, 
        ↑
           “1011”
         ↑


Output :  “0000”
Carry = 1

1.Take the input string of 0’s and 1’s (str1 , str2)




 1111 
↑ 
 1
↑
Index1 = -1
Index2 = -1
Carry = 1
Sum = 0
Output = ‘10000’





2. index1 = len(str1)-1
3. index2 = len(str2)-1
4. sum = 0
5. carry = 0
6. output = ‘’
In the loop : index1 >= 0 and index2 >= 0
sum = carry+int(str1[index1])+int(str2[index2])	
if(sum == 2)
sum = 0
carry = 1
if(sum == 3)
		sum == 1
		carry = 1
	output.insert(0,sum)
	index1 = index1-1
	index2 = index2-1

leftOverAddition(str1, index1, output)
leftOverAddition(str2, index2, output)


In the loop : index1 >= 0
		sum = carry+str1[index1]
		if(sum == 2)
sum = 0
carry = 1
output.insert(0,sum)
		index1 = index1-1
In the loop : index2 >= 0
		sum = carry+str2[index2]
		if(sum == 2)
sum = 0
carry = 1
output.insert(0,sum)
		index2 = index2-1
if(carry == 1)
	output.insert(0,carry)
return output

'''
def leftOverAddition(string,index,output,carry):
    '''
    In the loop : index >= 0
		sum = carry+string[index]
		if(sum == 2)
            sum = 0
            carry = 1
        output.insert(0,sum)
		index = index-1
	'''
    while(index >= 0):
        summ = carry+int(string[index])
        carry = 0
        if(summ == 2):
            summ = 0
            carry = 1
        output = str(summ)+output
        index = index-1
    return list((output,carry))
    
def binaryAddition(str1,str2):
    '''
    2. index1 = len(str1)-1
    3. index2 = len(str2)-1
    4. sum = 0
    5. carry = 0
    6. output = ‘’
    In the loop : index1 >= 0 and index2 >= 0
        sum = carry+int(str1[index1])+int(str2[index2])	
        if(sum == 2)
            sum = 0
            carry = 1
        if(sum == 3)
        	sum == 1
        	carry = 1
        output.insert(0,sum)
        index1 = index1-1
        index2 = index2-1
    leftOverAddition(str1, index1, output)
    leftOverAddition(str2, index2, output)
    if(carry == 1)
	    output.insert(0,carry)
    return output

    '''
    index1 = len(str1)-1
    index2 = len(str2)-1
    summ = 0
    carry = 0
    output = ''
    while(index1 >= 0 and index2 >= 0):
        summ = carry+int(str1[index1])+int(str2[index2])
        carry = 0
        if(summ == 2):
            summ = 0
            carry = 1
        if(summ == 3):
            summ = 1
            carry = 1
        print(summ,carry)
        output = str(summ)+output
        index1 = index1-1
        index2 = index2-1
    if(index1 >= 0):
        output_carry = leftOverAddition(str1, index1, output,carry)
        output = output_carry[0]
        carry = output_carry[1]
    if(index2 >= 0):
        output_carry = leftOverAddition(str2, index2, output,carry)
        output = output_carry[0]
        carry = output_carry[1]
    if(carry == 1):
        output = str(carry)+output
    return output
    
print(binaryAddition('1','1011'))


        

