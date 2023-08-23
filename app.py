import streamlit as st
from polish import polish_sentence_to_latin

st.title("Language Transliteration Interface")

input_string = st.text_input("Enter a Polish word/sentence to transliterate :")



if st.button("Transliterate"):
    if input_string:
        output_string = polish_sentence_to_latin(input_string)
        st.subheader("Transliterated Output:")
        st.write(output_string)
    else:
        st.warning("Please enter a string.")