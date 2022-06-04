import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)
        self.canal_1 = pygame.mixer.Channel(0)
        self.canal_2 = pygame.mixer.Channel(1)
        self.screen = pygame.display.set_mode()     
        self.size = self.screen.get_size()
        self.screen = pygame.display.set_mode(self.size)   
        self.clock = pygame.time.Clock()
        
        #si le jeu est en cours
        self.running = True
        #si on joue au jeu
        self.playing = False
        #si on est à l'écran titre
        self.menu = True
        #si on est dans les paramètres
        self.settings = False

        #font 
        self.body_font = pygame.font.SysFont('Open Sans', self.size[0]//40)
        self.head_font = pygame.font.SysFont('Open Sans', self.size[0]//10)
        self.subhead_font = pygame.font.SysFont('Open Sans', self.size[0]//15)
        #images
        self.logotext = pygame.image.load('data/img/logotext.png').convert_alpha()
        #musique + son
        self.menu_music = pygame.mixer.Sound("data/music/menu_music.mp3")
        self.clic = pygame.mixer.Sound("data/music/clic.mp3")

    def lobby(self):
        #fond vert
        self.screen.fill((1, 127, 123))
        #barre grise
        pygame.draw.rect(self.screen,(194, 190, 190),pygame.Rect(0,self.size[1]*0.95,self.size[0],self.size[1]*0.05))
        #texte barre grise
        self.screen.blit(
            self.body_font.render('A program proposed and sold by Memoria Entreprise', False, (255, 255, 255)),
            (self.size[0]//3.5,self.size[1]*0.95+10))
        #logo + texte
        self.screen.blit(
            pygame.transform.scale(self.logotext, (self.size[0]//3.5, self.size[0]//3.5)),
            (self.size[0]-self.size[0]//3.5,self.size[1]-self.size[0]//3.5))
        #bouton play
        btn_coll = [pygame.Rect(self.size[0]*0.06,self.size[1]*0.16,self.size[0]*0.3,self.size[1]*0.15),
                    pygame.Rect(self.size[0]*0.06,self.size[1]*0.38,self.size[0]*0.3,self.size[1]*0.15),
                    pygame.Rect(self.size[0]*0.06,self.size[1]*0.60,self.size[0]*0.3,self.size[1]*0.15)]
        pygame.draw.rect(self.screen,(1, 67, 127),btn_coll[0])
        self.screen.blit(
            self.head_font.render('PLAY', False, (255, 255, 255)),
            (self.size[0]*0.12,self.size[1]*0.19))
        #bouton settings        
        pygame.draw.rect(self.screen,(1, 67, 127),btn_coll[1])
        self.screen.blit(
            self.subhead_font.render('SETTINGS', False, (255, 255, 255)),
            (self.size[0]*0.10,self.size[1]*0.42))
        #bouton quit
        pygame.draw.rect(self.screen,(1, 67, 127),btn_coll[2])
        self.screen.blit(
            self.head_font.render('QUIT', False, (255, 255, 255)),
            (self.size[0]*0.12,self.size[1]*0.63))
        return btn_coll

    def update_lobby(self,coll):
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if coll[0].collidepoint(pos) and pressed1:
            self.canal_2.play(self.clic)
            print("Play")
        elif coll[1].collidepoint(pos) and pressed1:
            self.canal_2.play(self.clic)
            print("Settings")
        if coll[2].collidepoint(pos) and pressed1:
            self.canal_2.play(self.clic)
            self.running = False

    def run(self):
        self.canal_1.play(self.menu_music,-1)
        while self.running:
            if self.menu:
                self.update_lobby(self.lobby())


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)        

