
'''
>Convert the dict of dict into list of list such that every sublist contains values of all keys.
Output : 
[ 
  [ ‘Avdhoot’, ‘Namita’, ‘Anagha’, ‘Pooja’, Sanket’ ],
[30, 22, 42, 50, 35], 
[‘male’, ‘female’, ‘female’, ‘female’, ‘male’]
'''
main_dict = {'Patient1': {'name': 'Avdhoot', 'age': 30, 'gender': 'male', 'diagnosis': 'Dengue', 'Smoker': True}, 'Patient2': {'name': 'Pooja', 'age': 50, 'gender': 'female', 'diagnosis': 'TB', 'Smoker': True}, 'Patient3': {'name': 'Namita', 'age': 22, 'gender': 'female', 'diagnosis': 'Malaria', 'Smoker': True}, 'Patient4': {'name': 'Sanket', 'age': 35, 'gender': 'male', 'diagnosis': 'Corona', 'Smoker': False}, 'Patient5': {'name': 'Anagha', 'age': 42, 'gender': 'female', 'diagnosis': 'Dengue', 'Smoker': False}}

main_list = []
name_list = []
age_list = []
gender_list = []
diagnosis_list = []
Smoker_list = []

keys = []
for inner_dict in main_dict.values():
    for key in inner_dict.keys():
        keys.append(key)
    break
print(keys)
index = 0
for key in main_dict.keys():
    name_list.append(main_dict[key][keys[index]])
    age_list.append(main_dict[key][keys[index+1]])
    gender_list.append(main_dict[key][keys[index+2]])
    diagnosis_list.append(main_dict[key][keys[index+3]])
    Smoker_list.append(main_dict[key][keys[index+4]])
main_list.append(name_list)
main_list.append(age_list)
main_list.append(gender_list)
main_list.append(diagnosis_list)
main_list.append(Smoker_list)
print(main_list)



