import streamlit as st


def diz_ola(nome):
    st.write('Olá...')
    st.write(nome)


st.title("Olá GUI")
nome = st.text_input("Entre o seu nome e pressione o botão:")
if st.button("Diz"):
    if nome: 
        diz_ola(nome)
    else:
        st.write("Não entrou o seu nome!")