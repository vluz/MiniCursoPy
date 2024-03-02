#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st        # Biblioteca de interface gráfico
import languagemodels as lm   # Biblioteca de modelos linguísticos, faz todo o trabalho pesado


lm.set_max_ram('4gb')                  # Definir a memória RAM utilizável a 4 GB
st.title("LLM Minúsculo")              # Define o título e cria uma interface de utilizador
pergunta = st.text_input('Pergunta:')  # Obtem uma solicitação/pergunta/instrução do utilizador  
if pergunta:                           # Se houver uma pergunta, faz o seguinte:
    with st.spinner("a pensar..."):    #   Apresenta uma animação enquanto gera a resposta
        resposta = lm.do(pergunta)     #   Obtem resposta do modelo
    st.write(resposta)                 #   Escreve a resposta

