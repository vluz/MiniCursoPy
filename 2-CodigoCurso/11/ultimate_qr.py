#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
import segno
import streamlit as st
from urllib import parse, request


st.header("QR Code Animado", divider="rainbow")

qrurl = st.text_input("URL para o QR Code?")

question = st.text_input("Gif a procurar:")

if question:
    st.divider()
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode(
        {"api_key": "API_KEY_GOES_HERE", 
        "q": question, "limit": "4"}
    )

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())

    status = data["meta"]["status"]

    if status == 200:
        url0 = data["data"][0]["images"]["downsized"]["url"]
        url1 = data["data"][1]["images"]["downsized"]["url"]
        url2 = data["data"][2]["images"]["downsized"]["url"]
        url3 = data["data"][3]["images"]["downsized"]["url"]

        col0, col1, col2, col3 = st.columns(4)
        with col0:
            st.image(url0, caption="Imagem 0", width=100)
        with col1:
            st.image(url1, caption="Imagem 1", width=100)
        with col2:
            st.image(url2, caption="Imagem 2", width=100)
        with col3:
            st.image(url3, caption="Imagem 3", width=100)

        choice = st.radio(
            "Qual é a imagem a usar?", 
            ["0", "1", "2", "3"], 
            horizontal=True
        )

        if choice:
            if choice == "0":
                gifurl = url0
            elif choice == "1":
                gifurl = url1
            elif choice == "2":
                gifurl = url2
            elif choice == "3":
                gifurl = url3

            if st.button("Criar", type="primary"):
                st.divider()

                inow = time.strftime("%Y%m%d-%H%M%S")
                ifilename = inow + ".gif"

                ani_qrcode = segno.make_qr(qrurl)
                animation_url = request.urlopen(gifurl)
                ani_qrcode.to_artistic(
                    background=animation_url,
                    target=ifilename,
                    scale=10,
                )

                st.image(ifilename)
                st.write("Imagem gravada com o nome " + ifilename)

    else:
        st.write("Erro a obter GIFs")
