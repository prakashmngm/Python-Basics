main_dict = {'Patient1': {'name': 'Avdhoot', 'age': 30, 'gender': 'male', 'diagnosis': 'Dengue', 'Smoker': True}, 
    'Patient2': {'name': 'Pooja', 'age': 50, 'gender': 'female', 'diagnosis': 'TB', 'Smoker': True}, 
    'Patient3': {'name': 'Namita', 'age': 22, 'gender': 'female', 'diagnosis': 'Malaria', 'Smoker': True}, 
    'Patient4': {'name': 'Sanket', 'age': 35, 'gender': 'male', 'diagnosis': 'Corona', 'Smoker': False}, 
    'Patient5': {'name': 'Anagha', 'age': 42, 'gender': 'female', 'diagnosis': 'Dengue', 'Smoker': False}}
occupation = [ ("Avdhoot", "Teacher") , ("Namita", "Baker"), ("Anagha", "Banker") , ("Pooja", "IT")  , ("Sanket", "Business") ]  


'''
1. list out all the names from the given occupation list
2. list out all the occupations from the given occupation list
'''
names_list = []
occupation_list = []
for pair in occupation:
    index = 0
    names_list.append(pair[index])
    occupation_list.append(pair[index+1])
print(names_list)
print(occupation_list)

'''
3. compare names of the inner dictionary with the names list
4. take all the main keys for the given names
'''
main_dict_keys = []
for ele in names_list:
    for key,inner_dict in main_dict.items():
        if(ele == inner_dict['name']):
            main_dict_keys.append(key)
print(main_dict_keys)

'''
5 . insert to the main dictionary with the corresponding occupations from the occupation list
'''

index = 0
for main_key in main_dict_keys:
    main_dict[main_key]['occupation'] = occupation_list[index]
    index = index+1
for key in main_dict.keys():
    print(key,main_dict[key])

