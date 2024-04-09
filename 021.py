#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

'''import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()'''

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alison a Lenda")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()