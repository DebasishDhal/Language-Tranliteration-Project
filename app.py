import streamlit as st
from polish import polish_sentence_to_latin
from hungarian import hungarian_sentence_to_latin
from turkish import turkish_sentence_to_latin
from serbo_croatian import serbian_sentence_to_latin
from romanian import romanian_sentence_to_latin

from essential_generators import DocumentGenerator
from googletrans import Translator
import string
import re

def random_sentence(lang):
    gen = DocumentGenerator()
    translator = Translator()
    sentence=gen.sentence() #Generates a random but coherent sentence in English
    return str(translator.translate(sentence,dest=lang).text) #Translates the sentence to target language


tab1, tab2, tab3, tab4, tab5= st.tabs(["Polish/Polski", "Hungarian/Magyar", "Turkish/Türkçe", "Serbo-Croatian-Bosnian", "Romanian/Română"])
# tab1, tab3, tab4= st.tabs(["Polish/Polski", "Turkish/Türkçe", "Serbo-Croatian-Bosnian"])
# tab1, tab2, tab3 = st.tabs(["Polish/Polski", "Hungarian/Magyar", "Turkish/Türkçe"])

with tab1:
    st.header("Polish Transliteration")
    input_string_polish = st.text_area("Enter a Polish word/sentence to transliterate:")
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
    input_string_hungarian = st.text_area("Enter a Hungarian word/sentence to transliterate:")
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
    input_string_turkish = st.text_area("Enter a Turkish word/sentence to transliterate:")
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
    
    st.header("Serbo-Croatian-Bosnian Transliteration")
    input_string_serbian = st.text_area("Enter a Serbian/Croatian/Bosnian word/sentence in Latin or Cyrillic to transliterate:")
    serbian_examples = ["Српски језик је богат ћириличким алфабетом са словима као ш, ж, њ, ч, and ћ.",
                       "Čini se da hrvatski jezik ima mnogo složenih znakova",
                       "Bosna je najbolja zemlja na svijetu"]

    
    selected_example_sr = st.selectbox('Choose an example as demo', ['None',"Generate a random sentence"]+serbian_examples)

    if selected_example_sr != 'None':
        input_string_serbian = selected_example_sr

    if selected_example_sr == "Generate a random sentence":
        input_string_serbian = random_sentence("sr")
    
    if st.button("Transliterate Serbo-Croatian-Bosnian"):
        if input_string_serbian:
            output_string = serbian_sentence_to_latin(input_string_serbian)
            st.subheader("Transliterated Output:")
            if selected_example_sr == "Generate a random sentence" :
                st.write(input_string_serbian)
                st.write(output_string)
            else:
                st.write(output_string)
        else:
            st.warning("Please enter a string.")


with tab5:
    st.header("Romanian Tranlisteration")
    input_string_romanian = st.text_area("Enter a Romanian word/sentence for transliteration into simple Latin")
    romanian_examples = ["România este situată lângă Marea Neagră", "Moldova a folosit grafia chirilică pentru a scrie limba moldovenească", 
                        "Va multumim pentru vizita"]

    selected_example_ro = st.selectbox("Choose an example as demo", ['None', "Generate a random sentence"]+romanian_examples)

    if selected_example_ro != 'None':
        input_string_romanian = selected_example_ro
        
    if selected_example_ro == "Generate a random sentence" :
        input_string_romanian = random_sentence('ro')
        
    if st.button("Transliterate Romanian"):
        if input_string_romanian:
            output_string = romanian_sentence_to_latin(input_string_romanian)
            st.subheader("Transliterated Output:")
            if selected_example_ro == "Generate a random sentence" :
                st.write(input_string_romanian)
                st.write(output_string)
            else:
                st.write(output_string)
        else:
            st.warning("Please enter a string.")
