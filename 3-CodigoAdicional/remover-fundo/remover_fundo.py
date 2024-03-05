#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import streamlit as st
from PIL import Image
from rembg import remove


def main():
    """
    Função principal para remover o fundo de um ficheiro png
    """
    st.title("Remover Fundo")
    st.divider()
    uploaded_file = st.file_uploader("Ficheiro png para remover o fundo:", type="png")

    if uploaded_file:
        st.image(uploaded_file, caption='Original')
        if st.button("Remover"):
            with st.spinner("Removendo..."):
                input_image = Image.open(uploaded_file)
                output_image = remove(input_image)
                now = str(time.strftime("%Y%m%d-%H%M%S"))
                filename = now + ".png"
                output_image.save(filename)
                st.image(output_image, caption='Resultado')
                st.write("Imagem gravada em:", filename)

if __name__ == "__main__":
    main()
