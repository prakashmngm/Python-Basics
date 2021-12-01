'''
Take the input positive integer(num)
Start = 0
End = num
Index = 0
Mid = (start+end)/2
In the loop : True
    old_mid = mid
    mid = (start+end)/2
    Square = mid*mid
    if(square > num)
        End = mid
    Else
        Start = mid
    if(index > 0)
        if(integral part of old_mid == integral part of mid)
            if( two digits after decimal of old_mid == two digits after decimal of mid)
                Break
    index = index+1
Return mid

'''
import math
def decimalDigitComparision(deci1,deci2):
    str1 = str(deci1)
    str2 = str(deci2)
    index1 = str1.index('.')
    index2 = str2.index('.')
    sub_str1 = str1[index1+1:index1+20]
    sub_str2 = str2[index2+1:index2+20]
    #print('sub_str1',sub_str1)
    #print('sub_str2',sub_str2)
    if(sub_str1 == sub_str2):
        return True
    else:
        return False

def squareRoot(num):
    start = 0
    end = num
    index = 0
    mid = (start+end)/2
    while(True):
        old_mid = mid
        mid = (start+end)/2
        square = mid*mid
        if(square > num):
            end = mid
        else:
            start = mid
        if(index > 0):
            if(int(old_mid) == int(mid)):
                if(decimalDigitComparision(old_mid,mid)):
                    break
        index = index+1
    print(mid)
    mid = round(mid,3)
    return mid
    

for val in range(1,26):
    print(squareRoot(val),math.sqrt(val))

