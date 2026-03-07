import pygame
import sys
from sprites.sprite_classes import*
black=(0,0,0)
w=800
h=800
FPS=60
pygame.init()
window=pygame.display.set_mode((w,h))
pygame.display.set_caption('rpg')
clock=pygame.time.Clock()

from load import*
def restart():
    global player,playerg
    playerg=pygame.sprite.Group()
    player=Player(playerim['right'][0],(400,400))
    playerg.add(player)
def gamelvl():
    global player,playerg
    playerg.draw(window)
    playerg.update(dt,FPS,playerim)
    pygame.display.update()

def drawmap(mapFile):
    gamemap=[]
    with open(mapFile, 'r') as file:
        for i in range(10):
            gamemap.append(file.readline().replace('\n', '').split(','))
        pos = [0, 0]
        for i in range(10):
            pos[1] = i * 80
            for j in range(100):
                pos[0] = j * 80

restart()

while True:
    dt=clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
    window.fill(black)
    gamelvl()
