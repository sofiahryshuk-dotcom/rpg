import pygame
from script import*
playerim={'right':load_image('assets/images/player/right'),
          'up':load_image('assets/images/player/up'),
          'left':load_image('assets/images/player/left'),
          'down':load_image('assets/images/player/down')}
grassim=pygame.image.load('assets/images/blocks/grass.png').convert_alpha()
lavaim=pygame.image.load('assets/images/blocks/lava.png').convert_alpha()
rockim=pygame.image.load('assets/images/blocks/rock.png').convert_alpha()
sandim=pygame.image.load('assets/images/blocks/sand.png').convert_alpha()
waterim=pygame.image.load('assets/images/blocks/water.png').convert_alpha()