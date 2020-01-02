import pygame
import random,time

pygame.init()
pygame.mixer.init()


scr_width = 1200
scr_height = 700
win = pygame.display.set_mode((scr_width,scr_height))

gamemode = 20
backSpaceIngedrukt = 0
easteregg = False
playerSpeed = 6
all_sprites = pygame.sprite.Group()
touristen = pygame.sprite.Group()
dispFont = pygame.font.Font(pygame.font.get_default_font(), 50)
showMenu = True

hitSound = pygame.mixer.Sound('Hit_Hurt.wav')
deadSound = pygame.mixer.Sound('Powerup.wav')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fiets1.png')
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedLeft = playerSpeed
        self.speedRight = playerSpeed
        self.rect.y = (scr_height/4) + (scr_height/2)
        self.rect.x = 350
        self.levens = 5.0
        self.score = 0
        self.highScoreText = open('highscore.txt', 'r+')
        self.highScore = int(self.highScoreText.read(1))

    def update(self):
        self.highScoreText = open('highscore.txt', 'r+')
        self.highScore = int(self.highScoreText.read(1))
        self.highScore += 1
        self.highScoreText.write(str(self.highScore))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedRight
            self.speedLeft = playerSpeed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speedLeft
            self.speedRight = playerSpeed

        if self.rect.right > scr_width:
            self.speedRight = 0
        if self.rect.left < 0:
            self.speedLeft = 0

        if easteregg == False:
            self.score += 1

        drawScore = dispFont.render(str(self.score), True, (0, 0, 0))
        drawHighScore = dispFont.render(str(self.highScore), True, (0, 0, 0))
        drawScoreRect = drawScore.get_rect(center=(1100, 90))
        drawHighScoreRect = drawHighScore.get_rect(center=(100, 90))
        win.blit(drawScore, drawScoreRect)
        win.blit(drawHighScore, drawHighScoreRect)

        if keys[pygame.K_1]:
            gamemode = 20
        if keys[pygame.K_2]:
            gamemode = 22
        if keys[pygame.K_3]:
            gamemode = 24
        if keys[pygame.K_4]:
            gamemode = 26
        if keys[pygame.K_5]:
            gamemode = 28
        if keys[pygame.K_6]:
            gamemode = 30
        if keys[pygame.K_7]:
            gamemode = 32
        if keys[pygame.K_8]:
            gamemode = 34
        if keys[pygame.K_9]:
            gamemode = 36
        if keys[pygame.K_0]:
            gamemode = 38
'''
        self.highScoreText = open('highscore.txt', 'r+')
        self.highScoreText.write(self.highScore)
'''




class Tourist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enemyraden = random.randint(1,5)
        self.enemyimg = ' '
        if self.enemyraden == 1:
            self.enemyimg = 'enemy1.png'
        if self.enemyraden == 2:
            self.enemyimg = 'enemy2.png'
        if self.enemyraden == 3:
            self.enemyimg = 'enemy3.png'
        if self.enemyraden == 4:
            self.enemyimg = 'enemy1.png'
        if self.enemyraden == 5:
            self.enemyimg = 'enemy1.png'
        self.image = pygame.image.load(self.enemyimg)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,1200),-50)

    def update(self):
        self.rect.y += playerSpeed + 3

        if self.rect.y > scr_height:
            self.rect.y = -(random.randint(90,400))
            self.rect.x = random.randint(1,1200)
            tourist = Tourist()
            all_sprites.add(tourist)
            touristen.add(tourist)

        if len(touristen) > gamemode:
            self.kill()

        offset = (player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        result = player.image_mask.overlap(self.image_mask, offset)
        if result:
            hitSound.play()
            if easteregg == True:
                player.score += 1
            if easteregg == False:
                player.levens -= 1.0
            tourist = Tourist()
            all_sprites.add(tourist)
            touristen.add(tourist)
            self.kill()

class Menu():
    def __init__(self):
        self.title = dispFont.render('GAME OVER',True, (0,0,0))
        self.titleRect = self.title.get_rect(center=(scr_width/2,80))

        play = dispFont.render('PLAY', True, (0,0,0))
        button = pygame.Surface((250,125))
        self.buttonRect = button.get_rect()
        playRect = play.get_rect(center = self.buttonRect.center)
        self.buttonRect.center = (scr_width / 2, 440)
        button.fill((0,0,255))
        button.blit(play, playRect)
        self.button1 = button.copy()
        button.fill((0,0,0))
        play = dispFont.render('PLAY', True, (0,0,255))
        button.blit(play, playRect)
        self.button2 = button.copy()

        play = dispFont.render('QUIT', True, (0,0,0))
        button = pygame.Surface((250,125))
        self.buttonRect2 = button.get_rect()
        playRect = play.get_rect(center = self.buttonRect2.center)
        self.buttonRect2.center = (scr_width / 2, 590)
        button.fill((0,0,255))
        button.blit(play, playRect)
        self.button3 = button.copy()
        button.fill((0,0,0))
        play = dispFont.render('QUIT', True, (0,0,255))
        button.blit(play, playRect)
        self.button4 = button.copy()


    def draw(self, win):
        win.blit(self.title, self.titleRect)
        mouseover = self.buttonRect.collidepoint(pygame.mouse.get_pos())
        if mouseover:
            win.blit(self.button2, self.buttonRect)
        else:
            win.blit(self.button1, self.buttonRect)

        mouseover1 = self.buttonRect2.collidepoint(pygame.mouse.get_pos())
        if mouseover1:
            win.blit(self.button4, self.buttonRect2)
        else:
            win.blit(self.button3, self.buttonRect2)




player = Player()
all_sprites.add(player)

tourist = Tourist()
all_sprites.add(tourist)
touristen.add(tourist)