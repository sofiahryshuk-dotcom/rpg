import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos,colsp):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect(center=pos)
        self.colsp=colsp
        self.pos=pygame.Vector2(self.rect.center)
        self.direction=pygame.Vector2()
        self.speed=1500
        self.imdir='right'
        self.frame=0
        self.tanime=0
        self.anime=False
        self.item=False
    def input(self):
        keys=pygame.key.get_pressed()
        self.direction.x=0
        self.direction.y=0
        if keys[pygame.K_RIGHT]:
            self.direction.x=1
            self.imdir='right'
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.imdir = 'left'
        if keys[pygame.K_DOWN]:
            self.direction.y=1
            self.imdir='down'
        if keys[pygame.K_UP]:
            self.direction.y=-1
            self.imdir='up'
        if self.direction.length() !=0:
            self.direction=self.direction.normalize()
            self.anime=True
        else:
            self.anime=False

    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.collis('horizontal')

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        self.collis('vertical')

    def animation(self,FPS,playerim):
        if self.anime:
            self.tanime+=1
            self.image=playerim[self.imdir][self.frame]
            if self.tanime/FPS>0.1:
                if self.frame==len(playerim[self.imdir])-1:
                    self.frame=0
                else:
                    self.frame+=1
                self.tanime=0
    def update(self,dt,FPS,playerim):
        self.input()
        self.move(dt)
        self.animation(FPS,playerim)
    def collis(self,direction):
        for sprite in self.colsp:
            if sprite.rect.colliderect(self.rect):
                if direction=='horizontal':
                    if self.direction.x>0:
                        self.rect.right=sprite.rect.left
                    if self.direction.x<0:
                        self.rect.left = sprite.rect.right
                    self.pos.x=self.rect.centerx
                if direction=='vertical':
                    if self.direction.y>0:
                        self.rect.bottom=sprite.rect.top
                    if self.direction.y<0:
                        self.rect.top = sprite.rect.bottom
                    self.pos.y=self.rect.centery
    def mine(self,gamemap):
        for sprite in self.colsp:
            if sprite.rect.colliderect(self.rect.inflate(10,10)):
                if self.item and sprite.type=='rock':
                    i,j=sprite.tilep
                    gamemap[i][j]='0'
                    sprite.kill()




class Grass(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Lava(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type='water'

class Sand(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Rock(pygame.sprite.Sprite):
    def __init__(self, image, pos,tilep):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type='rock'
        self.tilep = tilep

class Crystal(pygame.sprite.Sprite):
    def __init__(self, image, pos,tilep):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.tilep=tilep

class Pick(pygame.sprite.Sprite):
    def __init__(self, image, pos,tilep):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.tilep=tilep






