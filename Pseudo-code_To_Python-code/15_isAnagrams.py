
def createDictionary(string,dictionary):
    '''
    index = 0
    In the loop : index < len(str1)
            if(str1[index] not in dict1)
                Dict1[str1[index]] = 1
            Else
                Dict1[str1[index]] = Dict1[str1[index]]+1
            Index = index+1
    '''
    
    index = 0
    while(index < len(string)):
        if(string[index] not in dictionary):
            dictionary[string[index]] = 1
        else:
            dictionary[string[index]] = dictionary[string[index]]+1
        index = index+1

def isAnagrams(str1,str2):
    '''
    Take two given input strings (str1 , str2)
    if(len(str1) != len(str2))
    Return False
    Dict1 = {}
    Dict2 = {}
    
    '''
    if(len(str1) != len(str2)):
        return False
    dict1 = {}
    dict2 = {}
    createDictionary(str1,dict1)
    createDictionary(str2,dict2)
    print(dict1)
    print(dict2)
    '''
    if(len(dict1) != len(dict2))
        Return False      
    In the loop : key1 , value1 in dict1.items()
                if(key1 in dict2)
                    if(value1 != dict2[key1])
                        Return False
                Else
                    Return False
    Return True
    
    '''
    if(len(dict1) != len(dict2)):
        return False
    for key1,value1 in dict1.items():
        if(key1 in dict2):
            if(value1 != dict2[key1]):
                return False
        else:
            return False
    return True

print(isAnagrams('222553','255232'))

