'''

Appending to the values of the dictonary.

'''

rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

rhymes_dict = {}
key = 0
for lst in rhymes:
    key = key+1
    rhymes_dict[key] = lst
print(rhymes_dict)

for k in rhymes_dict:
    rhymes_dict[k].append('blue')
    
print(rhymes_dict)

