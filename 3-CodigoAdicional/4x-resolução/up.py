#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import torch
import streamlit as st
from PIL import Image
from RealESRGAN import RealESRGAN


@st.cache_resource
def loadmodel():
    """
    Carrega o modelo RealESRGAN com o dispositivo e a escala especificados.
    
    Retorna:
    model: modelo RealESRGAN
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=4)
    model.load_weights('RealESRGAN_x4.pth', download=False)
    return model


def main():
    """
    Função principal para criar uma aplicação streamlit para aumentar a resolução de imagens.
    """
    st.title("Aumentar a resolução de imagem 4x")
    st.divider()
    uploaded_file = st.file_uploader("Imagem a elevar resolução:", type=["png", "jpg"])

    if uploaded_file:
        st.image(uploaded_file, caption='Original')
        if st.button("Elevar"):
            with st.spinner("A trabalhar..."):
                photo_input = Image.open(uploaded_file).convert('RGB')
                model = loadmodel()
                output = model.predict(photo_input)
                now = str(time.strftime("%Y%m%d-%H%M%S"))
                filename = now + ".png"
                output.save(filename)
                st.image(output, caption='Resultado')


if __name__ == "__main__":
    main()
