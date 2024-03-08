#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import pygame
import simpleaudio as sa


# Inicialização
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("musicloop.wav")
pygame.mixer.music.set_volume(0.3)

# Variáveis
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Encontra os pares")
FPS = 30
NUMBER_FONT = pygame.font.Font("icomoon.ttf", 55)
TEXT_FONT = pygame.font.SysFont("Arial", 55)
GREEN = (0, 150, 136)
WHITE = (236, 239, 241)
BLUE = (1, 87, 155)
BLACK = (38, 50, 56)
tiles = list(range(32)) * 2
state = {"mark": None}
show = [True] * 64
mclick = sa.WaveObject.from_wave_file("click.wav")
mclick2 = sa.WaveObject.from_wave_file("click2.wav")
mpair = sa.WaveObject.from_wave_file("makepair.wav")
mwin = sa.WaveObject.from_wave_file("wingame.wav")

# Randomização x2
random.shuffle(tiles)
random.shuffle(tiles)


def Numbering(x, y):
    for count in range(63, -1, -1):
        if (count % 8) * 75 < x < (count % 8 + 1) * 75 and (count // 8) * 75 < y < (
            count // 8 + 1
        ) * 75:
            return count


def darw_grid():
    rows = 8
    gap = WIDTH // rows
    for i in range(63, -1, -1):
        if show[i]:
            pygame.draw.rect(
                WIN, GREEN, (gap * (i % 8), gap * (i // 8), gap - 1, gap - 1), 1
            )
        else:
            pygame.draw.rect(WIN, BLUE, (gap * (i % 8), gap * (i // 8), gap, gap))


def reset():
    global show, tiles
    tiles = list(range(32)) * 2
    state = {"mark": None}
    show.clear()
    show = [True] * 64
    random.shuffle(tiles)
    pygame.mixer.music.play()


def redraw():
    WIN.fill(BLACK)
    darw_grid()


# Início
def main():
    global show
    run = True
    clickalt = True
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)
    while run:
        clock.tick(FPS)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mark = state["mark"]
                m_x, m_y = pygame.mouse.get_pos()
                spot = Numbering(m_x, m_y)
                if spot != None:
                    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
                        if clickalt == True:
                            mclick.play()
                            clickalt = False
                        else:
                            mclick2.play()
                            clickalt = True
                        state["mark"] = spot
                    else:
                        mpair.play()
                        clickalt = True
                        show[spot] = False
                        show[mark] = False
                        state["mark"] = None
            mark = state["mark"]
        if mark is not None and show[mark]:
            x, y = (mark % 8) * 75, (mark // 8) * 75
            text = NUMBER_FONT.render(chr(tiles[mark] + ord("!")), 1, WHITE)
            WIN.blit(text, (x + 10, y + 10))

        if show.count(False) == 64:
            WIN.fill(BLACK)
            pygame.mixer.music.stop()
            text = TEXT_FONT.render("VENCESTE!", 1, WHITE)
            WIN.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )
            mwin.play()
            pygame.display.update()
            pygame.time.delay(2000)
            reset()

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
