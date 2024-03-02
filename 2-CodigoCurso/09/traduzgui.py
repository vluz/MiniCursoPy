#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import deepl
import streamlit as st

# Definir o título para a aplicação Streamlit
st.title("TRADUTOR PARA INGLÊS")

# Inicializar o tradutor DeepL com a chave de API fornecida
translator = deepl.Translator("<CHAVE API AQUI>")

# Criar uma entrada de texto para o usuário inserir texto a ser traduzido
text = st.text_input("Texto a traduzir para Inglês:")

# Verificar se há algum texto de entrada
if text:
    # Traduzir o texto de entrada para inglês usando o tradutor DeepL
    result = translator.translate_text(text, target_lang="EN-GB")
    
    # Exibir a tradução
    st.write("Tradução:")
    st.write(result.text)

