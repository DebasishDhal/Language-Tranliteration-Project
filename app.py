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

tab1, tab2= st.tabs(["Polish", "Hungarian"])

with tab1:
    st.header("Polish Transliteration")
    input_string_polish = st.text_input("Enter a Polish word/sentence to transliterate:")
    polish_examples = ['Dziękuję bardzo!', 'Wszystkiego najlepszego!', 'Jarosław, Przemyśl']
    selected_example_po = st.selectbox('Choose an example as demo', ['None'] + polish_examples)

    if selected_example_po != 'None':
        input_string_polish = selected_example_po

    if st.button("Transliterate Polish"):
        if input_string_polish:
            output_string = polish_sentence_to_latin(input_string_polish)
            st.subheader("Transliterated Output:")
            st.write(output_string)
        else:
            st.warning("Please enter a string.")

with tab2:
    st.header("Hungarian Transliteration")
    input_string_hungarian = st.text_input("Enter a Hungarian word/sentence to transliterate:")
    hungarian_examples = ['Köszönöm szépen!', 'Nagyon szépen köszönjük','Budapest, Magyarország']
    selected_example_hu = st.selectbox('Choose an example as demo', ['None'] + hungarian_examples)

    if selected_example_hu != 'None':
        input_string_hungarian = selected_example_hu

    if st.button("Transliterate Hungarian"):
        if input_string_hungarian:
            output_string = hungarian_sentence_to_latin(input_string_hungarian)
            st.subheader("Transliterated Output:")
            st.write(output_string)
        else:
            st.warning("Please enter a string.")
            
                     