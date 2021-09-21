'''

Consider : 
rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]
-Count the no. of rhyming words in each sublist.
-Find the length of each word in the list.

'''

rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

'''
for index in range(len(rhymes)):
    count = 0
    for word_index in range(len(rhymes[index])):
        count = count+1
    words_count.append(count)
print(words_count)

'''
words_count = []
for lst in rhymes:
    words_count.append(len(lst))
print(words_count)

words_length = []
for lst in rhymes:
    inner_words_length = []
    for index in range(len(lst)):
        inner_words_length.append(len(lst[index]))
    words_length.append(inner_words_length)
print(words_length)
    

'''

Consider : 
rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

-Insert a new rhyming word for every sublist inside list.

'''

rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]


for lst in rhymes:
    word = input('enter a rhyming word that you want to insert:')
    lst.append(word)
print(rhymes)


'''

Consider : 
rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

-Create a new list such that every word will be in the ascending order of their length.

Expected Output : [be,he,cat,hat,fat,see,key,mouse,house,louse]

'''

rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

'''
1. create a list which consists of all the words from the given input list.
2. Find the length of the largest word in the list

'''

rhyming_words = []
largest_length = 0
for lst in rhymes:
    for ele in lst:
        if(largest_length < len(ele)):
            largest_length = len(ele)
        rhyming_words.append(ele)
print(rhyming_words)
print(largest_length)

'''
3. create a dictionary such that the key is the length of the word and value is the word

'''
rhyming_dict = {}
for ele in rhyming_words:
    rhyming_dict[len(ele)] = []
print(rhyming_dict)
for ele in rhyming_words:
    rhyming_dict[len(ele)].append(ele)
print(rhyming_dict)

'''
4. create a list based on the order of the length of the words in the created dictionary.

'''

key = 1
sorted_rhymes = []
while(key <= largest_length):
    if(key in rhyming_dict.keys()):
        for ele in rhyming_dict[key]:
            sorted_rhymes.append(ele)
    key = key+1
print(sorted_rhymes)




