def abbreviate(words):

    words = words.replace('-', ' ')
    words_array = words.split(' ')

    abbreviation = list()

    for word in words_array:

        index_counter = 0

        if word[0].isalnum():
            abbreviation.append((word[0]).upper())
            pass
        else:
            while word[index_counter].isalnum() == False:
                index_counter += 1
                if word[index_counter].isalnum():
                    abbreviation.append((word[index_counter]).upper())

    return ''.join(abbreviation)


words = 'The Road _Not_ Taken'
# Complementary metal-oxide semiconductor, 'CMOS'
# words = 'Complementary metal-oxide semiconductor'


def test(words):
    (abbreviate(words))
test(words)




# def abbreviate(words):
#
#     words_array = words.split(' ')
#
#     abbreviation = list()
#
#     for word in words_array:
#
#         index_counter = 0
#
#         if word[0].isalnum():
#             if '-' in word[0::]:
#                 hyphen_words = word.split('-')
#                 for item in hyphen_words:
#                     abbreviation.append((item).upper())
#                 pass
#
#             abbreviation.append((word[0]).upper())
#             pass
#         else:
#             while word[index_counter].isalnum() == False:
#                 index_counter += 1
#                 if word[index_counter].isalnum():
#                     abbreviation.append((word[index_counter]).upper())
#
#     return ''.join(abbreviation)


# words = 'The R_oad __Not__ _Ta_ken'
# Complementary metal-oxide semiconductor, 'CMOS'
words = 'Complementary metal-oxide semiconductor'


def test(words):
    print(abbreviate(words))
test(words)






# def abbreviate(words):
#
#     abbreviation = list()
#     abbreviation.append(words[0])
#
#     for index, letter in enumerate(words):
#         # print(letter)
#         if letter == '-' or '_':
#             pass
#
#         if letter == ' ':
#             if words[index+1] == '-' or words[index+1] == '_':
#                 pass
#             abbreviation.append((words[index+1]).upper())
#
#     return ''.join(abbreviation)

# https://exercism.io/my/solutions/73638553bbdf4acaa4ca696130ffa6ce


# def abbreviate2(words):
#
#     abbreviation = list()
#     abbreviation.append(words[0])
#
#     for index, letter in enumerate(words):
#
#         if letter == ' ':
            # if (words[index+1]).isalnum():
            #     abbreviation.append((words[index+1]).upper())
#             else:
#                 pass
#                 # if the next character after the space is not alphanumeric, then how do we grab the next possible alphanumeric
#     return ''.join(abbreviation)
