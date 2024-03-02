#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wikipedia

# Definir o idioma para Português
wikipedia.set_lang("pt")

# Obter a página da Wikipedia para "Barreiro"
result = wikipedia.page(title="Barreiro")
# Imprimir o conteúdo da página
print(result.content)

