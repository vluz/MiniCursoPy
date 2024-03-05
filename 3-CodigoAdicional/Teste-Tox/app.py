#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import pickle
import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization


def clean_text(text):
    """
    Limpa o texto de entrada removendo tags HTML, URLs, caracteres não alfabéticos
    e normalizando o texto para minúsculas.

    Args:
    text (str): O texto de entrada a ser limpo.

    Returns:
    str: O texto limpo.
    """
    text = re.sub(r'<[^>]+>', '', text)  # remove tags HTML
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z\'\s]', ' ', text)  # remove caracteres não alfabéticos
    text = re.sub(r'(\s)([iI][eE]|[eE][gG])(\s)', r' \2 ', text)  # normaliza "i.e." e "e.g."
    text = " ".join(text.split())  # remove espaços extras
    return text.lower()  # converte para minúsculas


@st.cache_resource
def load_model():
    """
    Carrega o modelo pré-treinado de classificação de comentários tóxicos.

    Returns:
    tf.keras.Model: O modelo carregado.
    """
    model = tf.keras.models.load_model(os.path.join("model", "toxmodel.keras"))
    return model


@st.cache_resource
def load_vectorizer():
    """
    Carrega o vetorizador de texto pré-treinado para o modelo de classificação de comentários tóxicos.

    Returns:
    TextVectorization: O vetorizador de texto carregado.
    """
    from_disk = pickle.load(open(os.path.join("model", "vectorizer.pkl"), "rb"))
    new_v = TextVectorization.from_config(from_disk['config'])
    new_v.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))  # correção para bug do Keras
    new_v.set_weights(from_disk['weights'])
    return new_v


st.title("Teste de Comentário Tóxico em Inglês")
st.divider()
model = load_model()
vectorizer = load_vectorizer()
default_prompt = "i love you man, but fuck you!"
input_text = st.text_area("Comentário em Inglês:", default_prompt, height=150).lower()
if st.button("Testar"):
    if not input_text:
        st.write("⚠ Aviso: Prompt vazio.")
    elif len(input_text) < 15:
        st.write("⚠ Aviso: O modelo é muito menos preciso com um prompt pequena.")
    if input_text == default_prompt:
        st.write("Os resultados esperados do comentário padrão são positivos para 0 e 2")
    with st.spinner("Testando..."):
        clean_input_text = clean_text(input_text)
        inputv = vectorizer([clean_input_text])
        output = model.predict(inputv)
        res = (output > 0.5)
    st.write(["tóxico", "muito tóxico", "obsceno", "ameaça", "insulto", "ódio de identidade"], res)
    st.write(output)