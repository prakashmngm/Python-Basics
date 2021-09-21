'''
Count no. of vowels & consonants per word

'''

rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]

'''
Finding out the vowel count and consonat count for each word in the given input list

'''

vowel_cons_dict = {}
for lst in rhymes:
    for word in lst:
        vowel_count = 0
        cons_count = 0
        for index in range(len(word)):
            if(word[index] == 'a' or word[index] == 'e' or word[index] == 'i' or word[index] == 'o' or word[index] == 'u'):
                vowel_count = vowel_count+1
            else:
                cons_count = cons_count+1
        #print('The word and their vowel count and consonant count are :',word,vowel_count,cons_count)
        vowel_cons_count = []
        vowel_cons_count.append(vowel_count)
        vowel_cons_count.append(cons_count)
        vowel_cons_dict[word] = vowel_cons_count
        #vowel_cons_dict[word] = list((vowel_count,cons_count))
print(vowel_cons_dict)

'''
Creating a dictionary such that the key is the word and the value is the list of vowel count and consonant counts.

'''

