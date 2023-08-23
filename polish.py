special_combs = {'szcz':'щ','Szcz':'Щ','ch':'х','Ch':'Х','cz':'ч','Cz':'Ч','dz':'ϳ','Dz':'Ј','dź':'ϳ','Dź':'Ј','dż':'ϳ','Dż':'Ј',
                'rz':'ж','Rz':'Ж','sz':'ш','Sz':'Ш','ż':'ж','Ż':'Ж','ź':'ж','Ź':'Ж','c':'ц','C':'Ц'}

polish_dict = {'a':'a','A':'A','ą':'an','Ą':'An','b':'b','B':'B','ć':'ch','Ć':'Ch','d':'d','D':'D','e':'e','E':'E','ę':'en',
                   'Ę':'En','f':'f','F':'F','g':'g','G':'G','h':'h','H':'H','i':'i','I':'I','j':'y','J':'Y','k':'k','K':'K',
                   'l':'l','L':'L','ł':'w','Ł':'W','m':'m','M':'M','n':'n','N':'N','ń':'ny','Ń':'Ny','o':'o','O':'O','ó':'u',
                   'Ó':'U','p':'p','P':'P','r':'r','R':'R','s':'s','S':'S','ś':'sh','Ś':'Sh','t':'t','T':'T','u':'u','U':'U',
                   'w':'v','W':'V','y':'y','Y':'Y','z':'z','Z':'Z'}

cyrillic_equiv_dict = {'щ':'sh','Щ':'Sh','х':'kh','Х':'Kh','ч':'ch','Ч':'Ch','ϳ':'j','Ј':'J','ж':'zh','Ж':'Zh', 'ш':'sh','Ш':'Sh',
                       'ц':'ts','Ц':'Ts'}

def check_special_comb(word):
    for comb in special_combs:
        if comb in word:
            word = word.replace(comb,special_combs[comb])
    return word


def polish_letter_to_eng(letter):
    if letter in polish_dict:
        return polish_dict[letter]
    else:
        return letter

def cyrillic_to_eng(word):
    for cyrillic in cyrillic_equiv_dict:
        if cyrillic in word:
            word = word.replace(cyrillic,cyrillic_equiv_dict[cyrillic])
    return word

def polish_sentence_to_latin(word):
    assert type(word)==str, "Input must be a string"
    #print("Original word: -",word)
    word = check_special_comb(word)
    #print("Just after special combination replacement: -",word)
    word = [polish_letter_to_eng(letter) for letter in word]
    word = ''.join(word)
    word = cyrillic_to_eng(word)
    return word
