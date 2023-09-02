special_combs = {
    'đ' : 'ъ', 'Đ' : 'Ъ',
    'ђ' : 'ъ', 'Ђ' : 'Ъ',
    'dž': 'ъ', 'Dž' : 'Ъ',
    'dz': 'ъ', 'Dz' : 'Ъ',
    'џ' : 'ъ', 'Џ' : 'Ъ',
    'c' : 'ts', 'C' : 'Ts',
}

serbian_dict = {
    'а': 'a', 'А' : 'A',
    'б': 'b', 'Б' : 'B',
    'в': 'v', 'В' : 'V',
    'г': 'g', 'Г' : 'G',
    'д': 'd', 'Д' : 'D',
    'е': 'e', 'Е' : 'E',
    'ж': 'zh', 'Ж' : 'Zh',
    'ž': 'zh', 'Ž' : 'Zh',
    'з': 'z', 'З' : 'Z',
    'и': 'i', 'И' : 'I',
    'ј': 'y', 'Ј' : 'Y',
    'j': 'y', 'J' : 'Y',
    'к': 'k', 'К' : 'K',
    'л': 'l', 'Л' : 'L',
    'љ': 'ly', 'Љ' : 'Ly',
    'lj': 'ly', 'Lj' : 'Ly',
    'м': 'm', 'М' : 'M',
    'н': 'n', 'Н' : 'N',
    'њ': 'ny', 'Њ' : 'Ny',
    'nj': 'ny', 'Nj' : 'Ny',
    'о': 'o', 'О' : 'O',
    'п': 'p', 'П' : 'P',
    'р': 'r', 'Р' : 'R',
    'с': 's', 'С' : 'S',
    'т': 't', 'Т' : 'T',
    'ћ': 'ch', 'Ћ' : 'Ch',
    'ć': 'ch', 'Ć' : 'Ch',
    'č': 'ch', 'Č' : 'Ch',
    'у': 'u', 'У' : 'U',
    'ф': 'f', 'Ф' : 'F',
    'х': 'h', 'Х' : 'H',
    
    'ч': 'ch', 'Ч' : 'Ch',
    # 'џ': 'dz', 'Џ' : 'Dz',
    'ш': 'sh', 'Ш' : 'Sh',
    'š': 'sh', 'Š' : 'Sh',
}

cyrillic_equiv_dict = {
    'ъ' : 'j', 'Ъ' : 'J',
    'ц': 'ts', 'Ц' : 'Ts',
}

def check_special_comb(word):
    for comb in special_combs:
        if comb in word:
            word = word.replace(comb,special_combs[comb])
    return word

def serbian_letter_to_eng(letter):
    if letter in serbian_dict:
        return serbian_dict[letter]
    else:
        return letter
    
def cyrillic_to_eng(word):
    for cyrillic in cyrillic_equiv_dict:
        if cyrillic in word:
            word = word.replace(cyrillic,cyrillic_equiv_dict[cyrillic])
    return word

def serbian_sentence_to_latin(sentence):
    sentence = str(sentence)
    # print("Original word: ", sentence)
    sentence = check_special_comb(sentence)
    # print("Just after special combination replacement: -", sentence)
    sentence = ''.join([serbian_letter_to_eng(letter) for letter in sentence])
    # print("After regular word replacement: -", sentence)
    sentence = cyrillic_to_eng(sentence)
    # print("Simplified pronunciation: -", sentence)
    return sentence