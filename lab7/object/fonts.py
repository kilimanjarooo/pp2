import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 72)

text = font.render("Hello, Dina", True, (0, 128, 0))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)