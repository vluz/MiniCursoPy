import deepl
import streamlit as st

st.title("TRADUTOR PARA INGLÊS")
translator = deepl.Translator("0aecf669-8335-928b-2673-1451d95c506c:fx")
text = st.text_input("Texto a traduzir para Inglês:")
if text:
    result = translator.translate_text(text, target_lang="EN-GB")
    st.write("Tradução:")
    st.write(result.text)