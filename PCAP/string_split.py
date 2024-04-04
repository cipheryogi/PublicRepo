# x = 'birdie*num*num!'
# y = x.split('*',maxsplit=1)
# z = x.split('*',maxsplit=2)
# print(f'{y},\n {z}')

# get_longest_word = 'Once I\'m awaken, I\'ll sacrifice your soul to the ruler of darkness.'
# m = get_longest_word.split(' ',maxsplit=200)
# n = []
# for el in range(len(m)):
#     n.append(m[el])
# longest = max(n,key=len)
# print(longest)

import re
# Input string
get_longest_word = 'Once I\'m awaken, I\'ll sacrifice your soul to the ruler of darkness.'
# Split the string based on spaces, commas, new line characters, and full stops
m = re.split(r'[ ,.\n]+', get_longest_word)
# Find the longest word
longest = max(m, key=len)
print("The longest word is:", longest)
