
list1 = [10,20,120,30,10,120,40,10,30,120,60,30,'sa',30,'sa','ri','sa']
print(len(list1))

dict1 = {}
for ele in list1:
    if ele not in dict1:
        dict1[ele] = None
print(dict1)
unique_list = []
for key in dict1.keys():
    unique_list.append(key)
print(unique_list)
  
count_list = []
for index in range(len(unique_list)):
    count_list.append(0)
print(count_list)


for ele in list1:
    index = 0
    while(index < len(unique_list)):
        if(ele == unique_list[index]):
            count_list[index] = count_list[index]+1
            break
        index = index+1
print(count_list)
print(unique_list[count_list.index(max(count_list))])
            


    


