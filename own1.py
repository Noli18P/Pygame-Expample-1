#Creare un juego sencillo usando los assets de el tutorial
#El juego consistirá en aparecer un "objeto" y al darle click obtener puntos y mostrarlo en por consola

import pygame
from sys import exit
import random

#window configuration
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Own 1")
clock = pygame.time.Clock()

#assets

background = pygame.image.load("graphics/Sky.png").convert_alpha()
ground = pygame.image.load("graphics/ground.png").convert_alpha()
fly_surf = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_rect = fly_surf.get_rect(topleft = (400, 20))
font = pygame.font.Font("font/Pixeltype.ttf",70)
text_surface = font.render('You Win!', False, "Green")


#game variables
clic = False
score = 0
to_win = random.randint(1, 30)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		#check mouse buttons
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos
			if fly_rect.collidepoint(mouse_pos):
				clic = True

	#spawn assets
	screen.blit(background, (0,0))
	screen.blit(ground,(0,300))
	screen.blit(fly_surf,fly_rect)
	
	#respwan
	if clic == True:
		new_x = random.randint(0,720)
		new_y = random.randint(0,220)
		clic = False
		fly_rect.topleft = (new_x, new_y)
		score += 1

	if score == to_win:
		fly_rect.topleft = (900,0)
		screen.blit(text_surface,(330, 80))
		



	pygame.display.update()
	clock.tick(60)