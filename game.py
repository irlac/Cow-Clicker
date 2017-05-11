import pygame
# import sys
# import time
# import random
# from pygame.sprite import Sprite

"""INIT"""

pygame.init()
pygame.mixer.init()

"""VARIABLES"""

display_width = 1067
display_height = 706
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cow Clicker')
clock = pygame.time.Clock()
FPS = 60
running = True
smallfont = pygame.font.SysFont('impact', 125)
medfont = pygame.font.SysFont('impact', 35)
bigfont = pygame.font.SysFont('impact', 50)
score = 999
score_text = 'Clicks: {0}'.format(score)
red = (237, 4, 4)
orange = (237, 113, 4)
yellow = (237, 186, 4)
green = (122, 206, 4)
blue = (4, 189, 206)
purple = (145, 4, 206)
pink = (242, 150, 236)
black = (0, 0, 0)
brown = (96, 78, 55)
white = (255, 255, 255)
cow = pygame.image.load_extended('cow.png')
cow_small = pygame.transform.scale(cow, (100, 100))
cow_super_small = pygame.transform.scale(cow, (32, 32))
pygame.display.set_icon(cow_super_small)

"""FUNCTIONS"""


def music():
    pygame.mixer.music.load('Silly Fun.mp3')
    pygame.mixer.music.play(-1)


def oof():
    effect = pygame.mixer.Sound('moo.wav')
    effect.play()


def end_music():
    pygame.mixer.music.load('boom_9.mp3')
    pygame.mixer.music.play(0)


def text_objects(text, color, font):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def msg_print(msg, color, y_displace, size):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


def bg_red():
        gameDisplay.fill(red)


def bg_orange():
        gameDisplay.fill(orange)


def bg_yellow():
        gameDisplay.fill(yellow)


def bg_green():
        gameDisplay.fill(green)


def bg_blue():
        gameDisplay.fill(blue)


def bg_purple():
        gameDisplay.fill(purple)


def bg_pink():
        gameDisplay.fill(pink)


def bg_colors():
    bg_red()
    # time.sleep(0.05)
    pygame.display.flip()
    bg_orange()
    clock.tick(FPS)
    pygame.display.flip()
    bg_yellow()
    clock.tick(FPS)
    pygame.display.flip()
    bg_green()
    clock.tick(FPS)
    pygame.display.flip()
    bg_blue()
    clock.tick(FPS)
    pygame.display.flip()
    bg_purple()
    clock.tick(FPS)
    pygame.display.flip()
    bg_pink()
    clock.tick(FPS)
    pygame.display.flip()
    y_displace = 0
    text_surf = smallfont.render(score_text, True, white)
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.flip()


def color_update():
    # gameDisplay.fill(blue)
    bg_colors()
    # pygame.display.flip()
    """time.sleep(0.01)
    gameDisplay.fill(red)
    pygame.display.flip()"""


def main_loop():
    global running
    global cow
    music()
    if score >= 1000:
        end_music()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_i:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_l:
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_e:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.KEYDOWN:
                                                                            if event.key == pygame.K_p:
                                                                                for event in pygame.event.get():
                                                                                    if event.type == pygame.KEYDOWN:
                                                                                        if event.key == pygame.K_s:
                                                                                            for event in pygame.event.get():
                                                                                                if event.type == pygame.KEYDOWN:
                                                                                                    if event.key == pygame.K_y:
                                                                                                        print('done')
                                                                                                        while 1 == 1:
                                                                                                            bg_colors()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pas = pygame.mouse.get_pos()
                if cow.get_rect().collidepoint(x, y):
                    gameDisplay.blit(cow_small, (pas[0] - 40, pas[1] - 40))
                    score = score + 1
                    bg_colors()
                    oof()

        game()
        global score
        global score_text
        score_text = 'Clicks: {0}'.format(score)
        pygame.display.flip()
        # text = smallfont.render(score_text, True, black)
        clock.tick(FPS)
        gameDisplay.fill(black)
        gameDisplay.blit(cow, [0, 0])
        y_displace = 0
        text_surf = smallfont.render(score_text, True, white)
        text_rect = text_surf.get_rect()
        text_rect.center = (display_width / 2), (display_height / 2) + y_displace
        gameDisplay.blit(text_surf, text_rect)

"""GAME LOOP"""


def game():
    global running
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

main_loop()
