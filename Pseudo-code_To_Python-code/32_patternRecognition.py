def patternRecognition(pattern,string):
    lst = string.split(' ')
    dict1 = {}
    index = 0
    while(index < len(pattern)):
        if(pattern[index] not in dict1):
            dict1[pattern[index]] = lst[index]
        index = index+1
    print(dict1)
    index = 0
    dict2 = {}
    while(index < len(lst)):
        if(lst[index] not in dict2):
            dict2[lst[index]] = pattern[index]
        index = index+1
    print(dict2)
    if(len(dict1) != len(dict2)):
        return False
    index = 0
    while(index < len(pattern)):
        if(dict1[pattern[index]] != lst[index]):
            return False
        index = index+1
    index = 0
    while(index < len(lst)):
        if(dict2[lst[index]] != pattern[index]):
            return False
        index = index+1
    return True
print(patternRecognition('babb','mo na mo mo'))
