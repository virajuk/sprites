import sys

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites = []
        self.sprites.append(pygame.image.load("graphics/sprites/0.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/1.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/2.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/3.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/4.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/5.png"))
        self.sprites.append(pygame.image.load("graphics/sprites/6.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def update(self, *args, **kwargs):

        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 1600, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SPRITES")

man_sprites = pygame.sprite.Group()
player = Player(150, 150)
man_sprites.add(player)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    man_sprites.draw(screen)
    man_sprites.update()
    pygame.display.flip()
    clock.tick(60)
