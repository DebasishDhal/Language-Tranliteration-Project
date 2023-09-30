from nltk.tokenize import word_tokenize

special_combs = {
    "Dzs" : "Ј", "dzs" : "ј",
    "Dz" : "Ъ", "dz" : "ъ", #Actually the sound of ds in kids
    "Cs" : "Ч", "cs" : "ч",
    "Zs" : "Ж", "zs" : "ж",
    "Sz" : "С", "sz" : "с",
    "Ly" : "y", "ly" : "y",
    "C"  : "Ц", "c"  : "ц",
    "Gy" : "Д", "gy" : "д",
    "A" : "А",   "a" : "а" #For the aw sound of Hungarian a sound. The value is the cyrillic а.
}

hungarian_dict = {
    "á" : "a", "Á" : "A",
    "é" : "i", "É" : "I",
    "í" : "i", "Í" : "I",
    "ó" : "o", "Ó" : "O",
    "ö" : "a", "Ö" : "A",
    "ő" : "a", "Ő" : "A",
    "ú" : "u", "Ú" : "U",
    "ü" : "ю", "Ü" : "Ю",
    "ű" : "ю", "Ű" : "Ю",
    "j" : "y", "J" : "Y",
    "s" : "sh", "S": "Sh"
}

cyrillic_equiv_dict = {
    "ъ" : "ds", "ь" : "Ds",
    "ч" : "ch", "Ч" : "Ch",
    "ж" : "zh", "Ж" : "Zh",
    "ш" : "sh", "Ш" : "Sh",
    "ј" : "j" , "Ј" : "J",
    "ю" : "yu", "Ю" : "Yu",
    "с" : "s" , "С" : "S",
    "ц" : "ts", "Ц" : "Ts",
    "д" : "d" , "Д" : "D",
    "а" : "aw", "А" : "Aw"
}

def check_special_comb(word):
    for comb in special_combs:
        if comb in word:
            word = word.replace(comb,special_combs[comb])
    return word

def hungarian_letter_to_eng(letter):
    if letter in hungarian_dict:
        return hungarian_dict[letter]
    else:
        return letter

def cyrillic_to_eng(word):
    for cyrillic in cyrillic_equiv_dict:
        if cyrillic in word:
            word = word.replace(cyrillic,cyrillic_equiv_dict[cyrillic])
    return word


def hungarian_sentence_to_latin(word):
    assert type(word)==str, "Input must be a string"
    # print("Original word: ", word)
    word = check_special_comb(word)
    # print("Just after special combination replacement: -",word)
    word = ''.join([hungarian_letter_to_eng(letter) for letter in word])
    # print("After regular word replacement: -",word)
    word = cyrillic_to_eng(word)
    # print("Simplified pronunciation: -",word)
    return word
