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
rcrystalim=pygame.image.load('assets/images/blocks/red_crystal.png').convert_alpha()
bcrystalim=pygame.image.load('assets/images/blocks/blue_crystal.png').convert_alpha()
pickim=pygame.image.load('assets/images/blocks/pick.png').convert_alpha()
npcim=load_image('assets/images/npc')
coinim=pygame.image.load('assets/images/blocks/coin0.png').convert_alpha()
npc2im=pygame.image.load('assets/images/enemy/2/1.png').convert_alpha()