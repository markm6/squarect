import pygame
import random
import math
import utils
from constants import *
from text import TextOptionMenu
import backgrounds.rectangles

clock = pygame.time.Clock()


def startup_menu(events):
    menu = TextOptionMenu(BASE_FONT, (255, 255, 255), (255, 100, 100), (20, 20), ["play", "options", "quit"])
    mouse_pos = pygame.mouse.get_pos()
    clock.tick(60)
    screen.fill((0, 0, 0))

    # first handle rects moving, shake etc
    backgrounds.rectangles.render_rects(screen)

    # render text & options next
    mouse_clicked = False
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
    hovered_opt, clicked_opt = menu.get_interacted(mouse_pos, mouse_clicked)
    if clicked_opt == 0:
        return 1
    elif clicked_opt == 1:
        return 2
    elif clicked_opt == 2:
        utils.quit_game()
    menu.blit(screen)
    pygame.display.update()
