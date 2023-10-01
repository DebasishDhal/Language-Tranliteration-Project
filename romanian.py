import re

special_combs = {
    "Este" : "Yeste", "este" : "yeste",
    "El" : "Yel", 
    "Che": "Ke", "che": "ke",
    "Chi": "Ki", "chi": "ki",
    "Ghe": "ଗେ", "ghe": "गे",
    "Ghi": "ଗି", "ghi": "गी",
    "Ch" : "h" , "ch" : "h",
    "Sc" : "Sk" , "sc" : "sk",
    "Ce" : "Чe", "ce" : "чe",
    "Ci" : "Чi", "ci" : "чi",
    "Ge" : "ଜେ", "ge" : "जे",
    "Gi" : "ଜି", "gi" : "जी",
}

romanian_dict = {
    "ă" : "aw", "Ă" : "Aw",
    "â" : "u", "Â" : "U",
    "î" : "u", "Î" : "U",
    "j" : "zh", "J" : "Zh",
    "q" : "k", "Q" : "K",
    "ș" : "sh", "Ș" : "Sh",
    "ț" : "ts", "Ț" : "Ts",
    "c" : "k", "C" : "K",
}

cyrillic_equiv_dict = {
    "ч" : "ch", "Ч" : "Ch",
    "ଗି" : "Gi", "गी": "gi",
    "ଗେ" : "Ge", "गे" : "ge",
    "ଜି" : "Ji", "जी" : "ji",
    "ଜେ" : "Je", "जे" : "je",
}

def romanian_position_conditional_replace(word):
    if len(word) == 1:
        return word
    
    if word.startswith("y"): 
        word = word.replace("y", "i",1)

    if word.startswith("Y"): 
        word = word.replace("Y", "I",1)
    
    if word.startswith("x"): #At beginning or word, x = ks
        word = word.replace("x", "ks",1)

    x_pattern = r'([aeiouAEIOU])(x)([aeiouAEIOU])' #x between vowels = ks
    replacement = r'\1gz\3'
    word = re.sub(x_pattern, replacement, word)

    if "x" in word or "X" in word:
        word = word.replace("x", "ks")
        word = word.replace("X", "Ks")

    return word

def check_special_comb(word):
    for key in special_combs.keys():
        if key in word:
            word = word.replace(key, special_combs[key])
    return word

def romanian_replace(word):
    for key in romanian_dict.keys():
        word = word.replace(key, romanian_dict[key])
    return word

def cyrillic_replace(word):
    for cyrillic in cyrillic_equiv_dict:
        if cyrillic in word:
            word = word.replace(cyrillic,cyrillic_equiv_dict[cyrillic])
    return word

def romanian_word_to_latin(word):
    word = romanian_position_conditional_replace(word)
    # print(word)
    word = check_special_comb(word)
    # print(word)
    word = romanian_replace(word)
    # print(word)
    word = cyrillic_replace(word)
    return word

def romanian_sentence_to_latin(text):
    tokens = text.split(" ")
    # print(tokens)
    latin_tokens = [romanian_word_to_latin(token) for token in tokens]
    # print(latin_tokens)
    latin_text = " ".join(latin_tokens)
    return latin_text