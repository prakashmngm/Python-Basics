
'''
Input will be a string, which is the attendance record of a student.
The string of length ‘n’, will have 3 diff alphabets ->
P : Present, A : Absent, L : Late.

Return Good if : a student is absent for less than 3 days
                      AND a student is never late for 3 or more consecutive days
                      AND no. of present days > 75%
Else return Bad.


Input -> 
AALLPL
APLLLA
PALLPA
ALLPAA
LLAPA

Output -> 
Bad
Bad
Bad
Bad
Bad



Take the input string
A_count = 0
L_count = 0
P_count = 0
In the loop : for every character of the input string
		if(char == ‘A’)
		 	A_count = A_count+1
		elif(char == ‘P’)
			P_count = P_count+1
		if(char == ‘L’)
			L_Consecutive_count = L_Consecutive_count+1
		else
			L_count = 0



if(A_count < 3 and L_Consecutive_count < 3 and P_count > (3/4)*len(string))
	Return Good
else
	Return Bad
'''

def goodOrBad(string):
    A_count = 0
    L_consecute_count = 0
    P_count = 0
    for char in string:
        if(char == 'A'):
            A_count = A_count+1
        elif(char == 'P'):
            P_count = P_count+1
        if(char == 'L'):
            L_consecute_count = L_consecute_count+1
        else:
            L_consecute_count = 0
        if(A_count >= 3 or L_consecute_count >= 3):
            return 'bad'
    if(A_count < 3 and L_consecute_count < 3 and P_count > (3/4)*len(string)):
        return 'good'
    else:
        return 'bad'

print(goodOrBad('PPPLAA'))
