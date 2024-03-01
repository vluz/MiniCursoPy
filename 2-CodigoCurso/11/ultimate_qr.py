#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
import segno
import streamlit as st
from urllib import parse, request

# Obter o URL para o Código QR
qr_url = st.text_input("Qual é a URL para o Código QR?")

# Obter o GIF a pesquisar
gif_to_search = st.text_input("Qual é o GIF a procurar?")

# Verificar se um GIF foi pesquisado
if gif_to_search:
    # Adicionar uma divisória
    st.divider()
    
    # Definir o URL do Giphy
    giphy_url = "http://api.giphy.com/v1/gifs/search"
    
    # Definir os parâmetros de pesquisa
    params = parse.urlencode(
        {"api_key": "<CHAVE API GIPHY AQUI>", 
        "q": gif_to_search, "limit": "4"}
    )
    
    # Fazer um pedido à API do Giphy
    with request.urlopen("".join((giphy_url, "?", params))) as response:
        data = json.loads(response.read())
    
    # Obter o estado da resposta
    status = data["meta"]["status"]

    # Verificar se o estado da resposta é 200
    if status == 200:
        # Extrair URLs para as imagens
        gif_urls = [data["data"][i]["images"]["downsized"]["url"] for i in range(4)]
        
        # Mostrar as imagens e permitir que o utilizador escolha uma
        cols = st.columns(4)
        for i in range(4):
            with cols[i]:
                st.image(gif_urls[i], caption=f"Imagem {i}", width=100)
        
        # Pedir ao utilizador para escolher uma imagem
        choice = st.radio(
            "Qual é a imagem a usar?", 
            ["0", "1", "2", "3"], 
            horizontal=True
        )
        
        # Verificar se o utilizador fez uma escolha
        if choice:
            # Obter o URL do GIF escolhido
            gif_url = gif_urls[int(choice)]
            
            # Verificar se o botão "Criar" foi clicado
            if st.button("Criar", type="primary"):
                # Adicionar uma divisória
                st.divider()
                
                # Criar o nome do ficheiro de imagem
                inow = time.strftime("%Y%m%d-%H%M%S")
                ifilename = inow + ".gif"
                
                # Gerar o código QR
                ani_qrcode = segno.make_qr(qr_url)
                
                # Abrir o URL do GIF escolhido
                animation_url = request.urlopen(gif_url)
                
                # Adicionar animação ao código QR e guardá-lo como GIF
                ani_qrcode.to_artistic(
                    background=animation_url,
                    target=ifilename,
                    scale=10,
                )
                
                # Mostrar a imagem gerada
                st.image(ifilename)
                st.write("Imagem gravada com o nome " + ifilename)
    else:
        # Mostrar uma mensagem de erro se houver um problema ao obter os GIFs
        st.write("Erro a obter GIFs")
