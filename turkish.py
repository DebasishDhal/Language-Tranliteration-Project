# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
import string

special_combs = {"c" : "ј", "C" : "Ј"} #These are Serbian J characters, they will be later converted to Latin J.

turkish_dict = {

"ç" : "ch" , "Ç" : "Ch",
"ğ" : "'" , "Ğ" : "'", 
"ı" : "e" , "I": "E", 
"i" : "i" , "İ": "I",
"j" : "zh" , "J": "zh",
"ö" : "o" , "Ö" : "O",
"ş" : "sh" , "Ş" : "Sh",
"ü" : "yu" , "Ü" : "Yu",
"w" : "v" , "W" : "V",
}

cyrillic_equiv_dict = {
    "ј" : "j" , "Ј" : "J",
    "ў" : "w"
}

def check_special_comb(word):
    for comb in special_combs:
        if comb in word:
            word = word.replace(comb,special_combs[comb])
    return word

def cyrillic_to_eng(word):
    for cyrillic in cyrillic_equiv_dict:
        if cyrillic in word:
            word = word.replace(cyrillic,cyrillic_equiv_dict[cyrillic])
    return word

def turkish_letter_to_eng(letter):
    if letter in turkish_dict:
        return turkish_dict[letter]
    else:
        return letter

def check_punc(word): #The pronunciation of some Turkish chars change if they're at the string end. However, puncutation marks like ., etc can hamper this.
    punc_list = list(string.punctuation)

    ending_punc = False
    how_many_punc_end = 0
    #Modify it such that even it there are > 1 puncutaiton marks at the word ending, it'll detect that
    
    for punc in punc_list:
        if word.endswith(punc):
            ending_punc = True
            break
    
    for i in range(1,len(word)):
        if word[-i] in punc_list:
            how_many_punc_end += 1

        if word[-i] not in punc_list:
            break
    return ending_punc, how_many_punc_end

    
def turkish_word_to_latin(word):
    assert type(word)==str

    last_letter = ""

    ending_punc, how_many_punc_end = check_punc(word) #If a word ends with a puncutation letter. "deniz." will be True. How many puncutation chars. "deniz!!!" = 3

    if ending_punc:
        last_letter = word[-1*how_many_punc_end:]
        word = word[:-1*how_many_punc_end]

    word = check_special_comb(word)

    if word.endswith("ı"):
        word = word[:-1] + "aў"
    if word.endswith("er"):
        word = word[:-2]+"ar"

    word = check_special_comb(word)

    word = ''.join([turkish_letter_to_eng(letter) for letter in word])
    word = cyrillic_to_eng(word)

    if last_letter: #If a punctuation mark is there in the original word, it'll be added here. 
        word = word + last_letter
    return word


def turkish_sentence_to_latin(sentence):
    # word_list = word_tokenize(sentence) #Nltk tokenizer didn't work out as it is also splitting by sep = "'" sometimes. İstanbul'u becomes İstanbul ' u
    word_list = sentence.split(" ")
    processed_word_list = []

    for word in word_list:
        try:
            input_word = word
            processed_word_list.append(turkish_word_to_latin(word))
        except:
            processed_word_list.append(input_word)

    return " ".join(processed_word_list)
