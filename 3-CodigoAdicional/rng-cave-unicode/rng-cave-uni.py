#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


# Constantes para as dimensões do mapa e símbolos
ALTURA = 40
LARGURA = 120
mapa = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]
JOGADOR = "@"  # Símbolo do jogador
TESOURO = "$"  # Símbolo do tesouro
ROCHA = "#"  # Símbolo da rocha
CANTO = "!"  # Símbolo do canto
PAREDE = "█"  # Símbolo da parede
CHAO = " "  # Símbolo do chão
PORTA1 = "\\"  # Símbolo da porta 1
PORTA2 = "/"  # Símbolo da porta 2


def caverna(inicio):
    """
    Gera uma caverna no mapa.

    Args:
    inicio: bool - indica se é a primeira caverna ou não
    """
    # Gera dimensões e posição aleatórias para a caverna
    largura = random.randint(5, 14)
    altura = random.randint(3, 8)
    esquerda = random.randint(1, LARGURA - largura - 2)
    topo = random.randint(1, ALTURA - altura - 2)

    # Verifica se a caverna se sobrepõe a azulejos de chão existentes
    for y in range(topo - 1, topo + altura + 2):
        for x in range(esquerda - 1, esquerda + largura + 2):
            if mapa[y][x] == CHAO:
                return

    # Coloca portas e cantos na caverna
    portas = 0
    porta_x, porta_y = 0, 0
    if not inicio:
        for y in range(topo - 1, topo + altura + 2):
            for x in range(esquerda - 1, esquerda + largura + 2):
                s = x < esquerda or x > esquerda + largura
                t = y < topo or y > topo + altura
                if s ^ t and mapa[y][x] == PAREDE:
                    portas += 1
                    if random.randint(0, portas - 1) == 0:
                        porta_x, porta_y = x, y
        if portas == 0:
            return

    # Coloca cantos, paredes e portas na caverna
    for y in range(topo - 1, topo + altura + 2):
        for x in range(esquerda - 1, esquerda + largura + 2):
            s = x < esquerda or x > esquerda + largura
            t = y < topo or y > topo + altura
            mapa[y][x] = CANTO if s and t else PAREDE if s ^ t else CHAO
    if portas > 0:
        mapa[porta_y][porta_x] = PORTA2 if random.randint(0, 1) else PORTA1

    # Coloca jogador ou tesouro na caverna
    for j in range(1 if inicio else random.randint(1, 6)):
        mapa[random.randint(topo, topo + altura - 1)][
            random.randint(esquerda, esquerda + largura - 1)
        ] = (
            JOGADOR
            if inicio
            else TESOURO
            if random.randint(0, 3) == 0
            else random.choice(["*","o","~","+"]) # inimigos ou npcs
        )


def principal():
    """
    Função principal para gerar o mapa e imprimi-lo.
    """
    random.seed()
    
    # Preenche o mapa com rochas
    for y in range(ALTURA):
        for x in range(LARGURA):
            mapa[y][x] = ROCHA
    
    # Gera cavernas e popula o mapa
    for j in range(1000):
        caverna(j == 0)
    
    # Imprime o mapa
    for b in range (LARGURA):
        print(ROCHA, end="")
    print()
    for y in range(ALTURA):
        for x in range(LARGURA):
            c = mapa[y][x]
            print(PAREDE if c == CANTO else c, end="")
            if x == LARGURA - 1:
                print()
    for b in range (LARGURA):
        print(ROCHA, end="")


if __name__ == "__main__":
    principal()
