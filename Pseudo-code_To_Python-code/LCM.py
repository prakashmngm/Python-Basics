'''
>Given pseudo code, convert it into Python code.

Even , Even
12 , 16
if both are even numbers , the output is 2


Even , Odd
12 , 15

check the divisors as odd numbers (3 , 5 , 7 ,9 ,11 , 13, 15 ---)

 
odd  , Odd
15 , 21

check the divisors as odd numbers (3 , 5 , 7 ,9 ,11 , 13, 15 ---)



1.Let a, b be two numbers. (4,6)
2. if(a%2 == 0 and b%2 == 0):  
        return 2
   else:
        k = min(a,b)
        i = 3
        In Loop:
            if a mod i == 0 AND b mod i == 0 
                break
            i = i+2
            if i > k, then break.

        if i>k, return 1
          else return i.

Input : 2,1
Output : 1

Input : 3,4
Output : 1

Input : 5,6
Output : 1

Input : 12,3
Output : 3

'''

def LCM(a,b):
    if(a%2 == 0 and b%2 == 0):
        return 2
    else:
        start = 3
        min_val = min(a,b)
        while(True):
            if((a%start) == 0 and (b%start) == 0):
                break
            start = start+2
            if(start > min_val):
                break
        if(start > min_val):
            return 1
        else:
            return start

print(LCM(15,325))
    
