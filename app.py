# import streamlit as st
# from polish import polish_sentence_to_latin

# st.title("Language Transliteration Interface")

# input_string = st.text_input("Enter a Polish word/sentence to transliterate :")

# example1 = "Dziękuję bardzo!"  # Example 1
# example2 = "Wszystkiego najlepszego!"  # Example 2
# example3 = "Jarosław, Przemyśl"

# selected_example = st.selectbox('Choose an example as demo',
#     ('None','Dziękuję bardzo!', 'Wszystkiego najlepszego!', 'Jarosław, Przemyśl'))

# if selected_example == 'Dziękuję bardzo!':
#     input_string = 'Dziękuję bardzo!'
# elif selected_example == 'Wszystkiego najlepszego!':
#     input_string = 'Wszystkiego najlepszego!'
# elif selected_example == 'Jarosław, Przemyśl':
#     input_string = 'Jarosław, Przemyśl'
# else:
#     input_string = input_string

    
# if st.button("Transliterate"):
#     if input_string:
#         output_string = polish_sentence_to_latin(input_string)
#         st.subheader("Transliterated Output:")
#         st.write(output_string)
#     else:
#         st.warning("Please enter a string.")

import streamlit as st
from polish import polish_sentence_to_latin
from hungarian import hungarian_sentence_to_latin
from turkish import turkish_sentence_to_latin
from serbo_croatian import serbian_sentence_to_latin


from essential_generators import DocumentGenerator
from googletrans import Translator

import re
from nltk.tokenize import word_tokenize


def random_sentence(lang):
    gen = DocumentGenerator()
    translator = Translator()
    sentence=gen.sentence() #Generates a random but coherent sentence in English
    return str(translator.translate(sentence,dest=lang).text) #Translates the sentence to target language


tab1, tab2, tab3, tab4= st.tabs(["Polish/Polski", "Hungarian/Magyar", "Turkish/Türkçe", "Serbo-Croatian-Bosniak"])

with tab1:
    st.header("Polish Transliteration")
    input_string_polish = st.text_input("Enter a Polish word/sentence to transliterate:")
    polish_examples = ['Dziękuję bardzo!', 'Wszystkiego najlepszego!', 'Jarosław, Przemyśl']
    selected_example_po = st.selectbox('Choose an example as demo', ['None', "Generate a random sentence"] + polish_examples)

    if selected_example_po != 'None':
        input_string_polish = selected_example_po

    if selected_example_po == "Generate a random sentence" :
        input_string_polish = random_sentence('pl')

    if st.button("Transliterate Polish"):
        if input_string_polish:
            output_string = polish_sentence_to_latin(input_string_polish)
            st.subheader("Transliterated Output:")
            if selected_example_po == "Generate a random sentence" :
                # st.write("Polish:"+input_string_polish+'Output:'+output_string)
                st.write(input_string_polish)
                st.write(output_string)
            else:
                st.write(output_string)
        else:
            st.warning("Please enter a string.")

with tab2:
    st.header("Hungarian Transliteration")
    input_string_hungarian = st.text_input("Enter a Hungarian word/sentence to transliterate:")
    hungarian_examples = ['Köszönöm szépen!', 'Nagyon szépen köszönjük','Budapest, Magyarország']
    selected_example_hu = st.selectbox('Choose an example as demo', ['None', "Generate a random sentence"] + hungarian_examples)

    if selected_example_hu != 'None':
        input_string_hungarian = selected_example_hu

    if selected_example_hu == "Generate a random sentence" :
        input_string_hungarian = random_sentence('hu')

    if st.button("Transliterate Hungarian"):
        if input_string_hungarian:
            output_string = hungarian_sentence_to_latin(input_string_hungarian)
            st.subheader("Transliterated Output:")
            if selected_example_hu == "Generate a random sentence" :
                st.write(input_string_hungarian)
                st.write(output_string)
            else:
                st.write(output_string)
        else:
            st.warning("Please enter a string.")
            
with tab3:

    st.header("Turkish Transliteration")
    input_string_turkish = st.text_input("Enter a Turkish word/sentence to transliterate:")
    turkish_examples = ["Müzik, ruhumuzu besler ve duygularımızı ifade etmemize yardımcı olur.", "İhtiyaçlarınıza uygun özel bir çözüm sunabiliriz",
                          "Türkiye'nin güzel şehirlerinden biri olan İstanbul'u ziyaret etmek istiyorum."]
    selected_example_tu = st.selectbox('Choose an example as demo', ['None', "Generate a random sentence"] + turkish_examples)

    if selected_example_tu != 'None':
        input_string_turkish = selected_example_tu

    if selected_example_tu == "Generate a random sentence" :
        input_string_turkish = random_sentence('tr')
        
    if st.button("Transliterate Turkish"):
        if input_string_turkish:
            output_string = turkish_sentence_to_latin(input_string_turkish)
            st.subheader("Transliterated Output:")
            if selected_example_tu == "Generate a random sentence" :
                st.write(input_string_turkish)
                st.write(output_string)
            else:
                st.write(output_string)
        else:
            st.warning("Please enter a string.")

with tab4:
    st.header("Serbo-Coratian-Bosniak Transliteration")
    input_string_serbian = st.text_input("Enter a Serbian/Croatian/Bosniak word/sentence in Latin or Cyrillic to transliterate")
    serbian_examples = ["Српски језик је богат ћириличким алфабетом са словима као ш, ж, њ, ч, and ћ.",
                       "Čini se da hrvatski jezik ima mnogo složenih znakova",
                       "Bosna je najbolja zemlja na svijetu"]
    selected_example_sr = st.selectbox('Choose an example',[None]+serbian_examples)

    if selected_example_sr != ' None':
        input_string_serbian = selected_example_sr
        
    if st.button("Transliterate Serbo-Croatian-Bosniak"):
        if input_string_serbian:
            output_string = serbian_sentence_to_latin(input_string_serbian)
            st.subheader("Transliterated Output")
            st.write(output_string)

        else:
            st.warning("Please enter a string")
            