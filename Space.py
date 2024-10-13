import pygame
import random




pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Invader")

Yellow = (255,255,0)

Red = (255,0,0)
Fire_rad = 10
Fire_x = 150
Fire_y = 200
Fire_Speed = 10
Space_x = 200
Space_y = 300
ship_h = 40
ship_w = 25



while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit()

    screen.fill((0,0,0))
    pygame.draw.circle(screen,Yellow,(Fire_x,Fire_y),Fire_rad)
    pygame.draw.rect(screen,Red,(Space_x,Space_y,ship_h,ship_w))
    Fire_y = Fire_y+Fire_Speed
    if(Fire_y>500):
        Fire_y=0
        Fire_x=random.randint(20,380)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Space_x = Space_x+10

    if keys[pygame.K_LEFT]:
        Space_x = Space_x-10
    if Fire_x == Space_x and Fire_y == Space_y:
        screen.fill((0,255,0))

    pygame.time.delay(15)
    pygame.display.flip()