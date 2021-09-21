'''
>In the dict of dict, delete entries of patients that are ‘Non-Smoker’
OR age>40
'''

main_dict = {'Patient1': {'name': 'Avdhoot', 'age': 30, 'gender': 'male', 'diagnosis': 'Dengue', 'Smoker': True}, 
    'Patient2': {'name': 'Pooja', 'age': 50, 'gender': 'female', 'diagnosis': 'TB', 'Smoker': True}, 
    'Patient3': {'name': 'Namita', 'age': 22, 'gender': 'female', 'diagnosis': 'Malaria', 'Smoker': True}, 
    'Patient4': {'name': 'Sanket', 'age': 35, 'gender': 'male', 'diagnosis': 'Corona', 'Smoker': False}, 
    'Patient5': {'name': 'Anagha', 'age': 42, 'gender': 'female', 'diagnosis': 'Dengue', 'Smoker': False}}
    
main_dict_keys = []    
for key,inner_dict in main_dict.items():
    if((inner_dict['Smoker'] == False) or (inner_dict['age'] > 40)):
        main_dict_keys.append(key)
print(main_dict_keys)
for key in main_dict_keys:
    del main_dict[key]
for key in main_dict.keys():
    print(key,main_dict[key])
