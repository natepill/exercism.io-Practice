def abbreviate(words):

    abbreviation = list()
    abbreviation.append(words[0])

    for index, letter in enumerate(words):
        # print(letter)
        if letter == ' ':
            abbreviation.append(words[index+1])

    return ''.join(abbreviation)

# https://exercism.io/my/solutions/73638553bbdf4acaa4ca696130ffa6ce


# words = 'Jake Went Out'
#
# def test(words):
#     print(abbreviate(words))
#
# test(words)
