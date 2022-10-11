import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()