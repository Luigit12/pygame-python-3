import pygame
import random
import time
import classes
pygame.init()

win = pygame.display.set_mode((classes.scr_width,classes.scr_height))
pygame.display.set_caption('game')

clock = pygame.time.Clock()
FPS = 60
showMenu = classes.showMenu
background1 = pygame.image.load('background1.png')
menu = classes.Menu()

run = True
while run:
    clock.tick(FPS)
    if showMenu == True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    showMenu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.buttonRect2.collidepoint(pygame.mouse.get_pos()):
                    run = False


        win.fill((255,255,255))
        menu.draw(win)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        win.fill((255,255,255))
        win.blit(background1,(0,0))

        if classes.player.levens < 1.0:
            classes.player.score = 0
            classes.deadSound.play()
            showMenu = True
            classes.player.levens = 5.0

        if classes.easteregg == True:
            if classes.player.score > 300:
                classes.easteregg = False

        if keys[pygame.K_BACKSPACE] and keys[pygame.K_CAPSLOCK] and classes.backSpaceIngedrukt == 0:
            classes.backSpaceIngedrukt = 1
            classes.easteregg = True

        if keys[pygame.K_ESCAPE]:
            showMenu = True

        pygame.draw.rect(win, (0, 0, 0), [400, 50, 500, 50])
        pygame.draw.rect(win, (255,0,0), [400,50,classes.player.levens * 100,50])
        classes.all_sprites.update()
        classes.all_sprites.draw(win)
    pygame.display.update()
pygame.quit()