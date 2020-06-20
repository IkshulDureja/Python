import re

# patterns = ['term1','term2']
#
# text = 'This is a string with term1, not the other!'
#
# # for pattern in patterns:
# #     print("I'm searching for: "+pattern)
# match = re.search('term1', text)
#
# print(type(match))
# # The type is that of an object which has al the information about the pattern
#     #     print("MATCH!")
#     # else:
#     #     print("NO MATCH!")
#
#
# print(match.start())
#
# print(match.end())
#
# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term, email))
#
# print(re.findall('match','test phrase match in the middle match'))


def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        # print(pat.findall(phrase))
        print("\n")

#
# repition syntax
# A pattern followed by meta character * is repeated 0 or more times
test_phrase = 'sdsd..sssddd.sdddsddd...dsds...dsssss...sddddd'

# test_patterns = ['sd*']
# We want to find a s followed by 0 or more d

# if we want it followed by 1 or more d, we put a + sign
test_patterns = ['sd+']

# if we want it 0 or 1 time, we put a ?
# test_patterns = ['sd?']

# if we want to define a specific count
# test_patterns = ['sd{3}']
# test_patterns = ['sd{1,3}'] looking for 2 or 3 d


# when s is followed by EITHER 1 or more s OR 1 or more d
# test_patterns = ['s[sd]+']
multi_re_find(test_patterns, test_phrase)




# use ^ for exclusion
test_phrase1 = "This is a string! But it has punctuation. How can we remove it?"
test_pattern1 = ['[^!.? ]+']

multi_re_find(test_pattern1,test_phrase1)

# re.findall('[^!.? ]+',test_phrase1)
#
# to get a sequence of all the lower case characters, pattern = ['[a-z]']
# to get a sequence of all the upper case characters, pattern = ['[A-Z]']
# check out notes for more of these patterns, example one upper case followed by a lower case etc
# but we wont often use these codes

#
# special escape codes to find special patterns in your data such as digits, non digits, white space and more
# those are indicated using backspace

test_patterns2= [r'\d+']
# lower case d is a special character code to search for digits
test_phrase2 = 'This is a string with numbers 12312 and a symbol #hastag'

# Upper case D for non-digits
# lower case s for sequence of white space
 # upper case S for all the non whitespace
 #  lower case w for alpha numeric characters i.e. all the letters and numbers
  # upper case w for non alpha numeric i.e. # and spaces
