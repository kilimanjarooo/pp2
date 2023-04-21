import pygame, sys
pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

x = 47
y = 47

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()

        screen.fill((255, 255, 255))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 25: y -= 1
        if pressed[pygame.K_DOWN] and y < 275: y += 1
        if pressed[pygame.K_LEFT] and x > 25: x -= 1
        if pressed[pygame.K_RIGHT] and x < 375: x += 1

        pygame.draw.circle(screen, 'red', (x, y), 25)
        pygame.display.flip()
        clock.tick(120)

pygame.quit()