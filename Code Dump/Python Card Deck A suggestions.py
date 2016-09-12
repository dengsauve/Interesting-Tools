### SUGGESTIONS!!! ###
lines = [
    ['┌─────────┐'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['└─────────┘']
]

########################################################################################################################

def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    lines = ['┌─────────┐'] + ['│░░░░░░░░░│'] * 7 + ['└─────────┘']

    cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)

    return '\n'.join([x + y for x, y in zip(lines, cards_except_first)])

##########################################################################################################################

result = []
for index, line in enumerate(lines):
	result.append(''.join(lines[index]))



    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)

Can be simplified to this:

return '\n'.join([''.join(line) for line in lines])




