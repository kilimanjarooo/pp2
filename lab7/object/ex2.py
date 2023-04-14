import pygame
import os

screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()

clock = pygame.time.Clock()

x = 30
y = 30
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                      is_blue = not is_blue

        screen.fill((255, 255, 255))
        screen.blit(get_image('lab7/object/ball.png'), (20, 20))
        #effect = pygame.mixer.Sound('lab7/object/1.mp3')
        play_sound("lab7/object/1.mp3")
        pygame.display.flip()
        clock.tick(120)