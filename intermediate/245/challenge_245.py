"""
Question:
https://www.reddit.com/r/dailyprogrammer/comments/3x3hqa/20151216_challenge_245_intermediate_ggggggg_gggg/
"""


# Part 1 - made a decoder function
def alien_to_english(key_string):
    """
    function that takes in the key string and makes a lookup dictionary
    for the string
    """
    letter = None
    letter_to_dict = {}
    for i, item in enumerate(key_string.split(" ")):
        if i % 2 == 0:
            letter = item
        else:
            letter_to_dict[item] = letter
    return letter_to_dict


def translate_from_alien(key_string, alien_sentence):
    """
    function that takes in the key string and the sentence and translates it
    """
    converter_dict = alien_to_english(key_string)

    decoded = ""
    letter = ""
    for l in alien_sentence:
        if l == "G" or l == "g":
            letter += l
            if letter in converter_dict:
                # if it is found convert it
                decoded += converter_dict[letter]
                letter = ""
        else:
            decoded += l
    return decoded


key = "a GgG d GggGg e GggGG g GGGgg h GGGgG i GGGGg l GGGGG m ggg o GGg p Gggg r gG y ggG"
message = "GGGgGGGgGGggGGgGggG /gG/GggGgGgGGGGGgGGGGGggGGggggGGGgGGGgggGGgGggggggGggGGgG!"

assert(translate_from_alien(key, message) == "hooray /r/dailyprogrammer!")


# part 2 - make it so you can convert to gg language

def english_to_alien(sentence):
    import math
    set_of_chars = set(char for char in sentence if char.isalpha())
    max_len = int(math.ceil(math.log(len(set_of_chars), 2)))

    # for converting alien to english
    conversion_dict = {}

    for i, char in enumerate(set_of_chars):
        binary_str = str(bin(i))[2:]
        binary_str = binary_str.replace("0", "g").replace("1", "G")
        alien_char = "g" * (max_len - len(binary_str)) + binary_str
        conversion_dict[char] = alien_char

    return conversion_dict

def translate_to_alien(sentence):
    # make translation dictionary
    translation_dict = english_to_alien(sentence)
    # make translate string
    translation_string = " ".join([
        k + " " + v
        for k, v in translation_dict.iteritems()
    ])
    # make alien sentence
    alien_sentence = ""
    for l in sentence:
        if l.isalpha():
            alien_sentence += translation_dict[l]
        else:
            alien_sentence += l
    return translation_string, alien_sentence


# test function
def test_part_2(string):
    # same thing should be returned
    key, message = translate_to_alien(string)
    assert(translate_from_alien(key, message) == string)

# all of these should pass
test_part_2("Hi")
test_part_2("Hello, world!")
jackdaw_txt = """
Here's the thing. You said a "jackdaw is a crow."
Is it in the same family? Yes. No one's arguing that.
As someone who is a scientist who studies crows, I am telling you, specifically, in science, no one calls jackdaws crows. If you want to be "specific" like you said, then you shouldn't either. They're not the same thing.
If you're saying "crow family" you're referring to the taxonomic grouping of Corvidae, which includes things from nutcrackers to blue jays to ravens.
So your reasoning for calling a jackdaw a crow is because random people "call the black ones crows?" Let's get grackles and blackbirds in there, then, too.
Also, calling someone a human or an ape? It's not one or the other, that's not how taxonomy works. They're both. A jackdaw is a jackdaw and a member of the crow family. But that's not what you said. You said a jackdaw is a crow, which is not true unless you're okay with calling all members of the crow family crows, which means you'd call blue jays, ravens, and other birds crows, too. Which you said you don't.
It's okay to just admit you're wrong, you know?
"""
test_part_2(jackdaw_txt)
