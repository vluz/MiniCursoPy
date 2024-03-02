#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import ipaddress
import pandas as pd
import streamlit as st
from requests import get
from ip2geotools.databases.noncommercial import DbIpCity, HostIP

def getlocbyip(ip):
    """
    Obtém latitude e longitude do endereço IP fornecido usando ip2geotools.

    Args:
    ip (str): Endereço IP a ser pesquisado.

    Returns:
    tuple: Latitude e longitude do endereço IP.
    """
    try:
        res = DbIpCity.get(ip, api_key="free")
        return res.latitude, res.longitude
    except Exception as e:
        print(getattr(e, 'message', repr(e)))
        try:
            res = HostIP.get(ip)
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            st.write("Erro na localização.")
        return 0, 0

def isvalidip(ip):
    """
    Verifica se a string fornecida é um endereço IP válido.

    Args:
    ip (str): Endereço IP a ser validado.

    Returns:
    bool: True se o endereço IP for válido, False caso contrário.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except Exception as e:
        print(getattr(e, 'message', repr(e)))
        return False

def getmyip():
    """
    Obtém o endereço IP público da máquina atual.

    Returns:
    str: Endereço IP público da máquina atual.
    """
    try:
        myip = get("https://api.ipify.org").content.decode("utf8")
    except Exception as e:
        print(getattr(e, 'message', repr(e)))
        myip = "0.0.0.0"
    return myip

# Interface do Streamlit
st.header("Localização de endereço IP", divider="rainbow")
ip = st.text_input("Endereço IP:", getmyip())
if st.button("Obter localização", type="primary"):
    if isvalidip(ip):
        try:
            st.write("Nome do host: " + socket.gethostbyaddr(ip)[0])
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            st.write("O nome para este IP não foi encontrado.")
        with st.spinner("A localizar..."):
            lat, lon = getlocbyip(ip)
            st.write("Lat: " + str(lat) + "   Lon: " + str(lon))
            data = pd.DataFrame({"latitude": [lat], "longitude": [lon]})
            st.map(data, color="#ff000088", zoom=12)
            st.write("ATENÇÃO: Localização pode estar errada.")
    else:
        st.write("O IP \"" + ip + "\" não é válido")

