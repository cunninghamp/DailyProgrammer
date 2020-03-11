import string


def smorse(word):
    # Create a variable for the output
    output = ""

    # Create a list from the characters of the input word
    lettersinword = list(word)

    # Loop through list and concatenate the corresponding morse code to the output
    for i in lettersinword:
        output = output + (morse[alphabet.index(i)])

    # I've added this for nicer reading
    output = "The morse code for " + word + " is " + output
    return output


# Create a list of the letters a-z
alphabet = list(string.ascii_lowercase)

# Create a list of the individual characters of morse code provided by the challenge
morsecodes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morse = list(morsecodes.split(" "))


print(smorse("sos"))
print(smorse("daily"))
print(smorse("programmer"))
print(smorse("bits"))
print(smorse("three"))
