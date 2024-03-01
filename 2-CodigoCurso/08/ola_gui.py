#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st

def diz_ola(nome):
    """
    Função que escreve 'Olá...' e exibe cada letra do nome fornecido.

    Args:
    nome (str): O nome a ser cumprimentado.
    """
    st.write('Olá...')
    for letter in nome:
        st.write(letter)

# Define o título da interface
st.title("Olá GUI")

# Solicita e captura o nome do usuário
nome = st.text_input("Entre o seu nome e pressione o botão:")

# Verifica se o botão foi pressionado
if st.button("Diz"):
    # Verifica se o nome foi fornecido
    if nome: 
        diz_ola(nome)
    else:
        st.write("Não entrou o seu nome!")