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
from camera import Camera

from load import*
def restart():
    global player,playerg,sandg,waterg,lavag,grassg,rockg,scrollg,rcrystalg,bcrystalg,camera
    playerg=pygame.sprite.Group()
    player=Player(playerim['right'][0],(400,400))
    playerg.add(player)
    sandg=pygame.sprite.Group()
    waterg=pygame.sprite.Group()
    lavag=pygame.sprite.Group()
    grassg=pygame.sprite.Group()
    rockg=pygame.sprite.Group()
    scrollg=pygame.sprite.Group()
    rcrystalg=pygame.sprite.Group()
    bcrystalg = pygame.sprite.Group()
    camera=Camera(8000,8000,w,h)
def gamelvl():
    global player,playerg,waterg,grassg,lavag,sandg,rockg,scrollg,rcrystalg,bcrystalg,camera
    waterg.draw(window)
    grassg.draw(window)
    lavag.draw(window)
    sandg.draw(window)
    rockg.draw(window)
    rcrystalg.draw(window)
    bcrystalg.draw(window)
    playerg.draw(window)
    playerg.update(dt, FPS, playerim)
    camera.update(player,window,scrollg)
    pygame.display.update()





def drawmap(mapFile):
    global sandg,waterg,grassg,rockg,lavag,scrollg,rcrystalg,bcrystalg,camera
    gamemap=[]
    with open(mapFile, 'r') as file:
        for i in range(100):
            gamemap.append(file.readline().replace('\n', '').split(','))
        pos = [0, 0]
        for i in range(100):
            pos[1] = i * 80
            for j in range(100):
                pos[0] = j * 80

                if gamemap[i][j] == '0':
                    grass = Grass(grassim, pos)
                    grassg.add(grass)
                    scrollg.add(grass)

                if gamemap[i][j] == '4':
                    water = Water(waterim, pos)
                    waterg.add(water)
                    scrollg.add(water)

                if gamemap[i][j] == '3':
                    sand = Sand(sandim, pos)
                    sandg.add(sand)
                    scrollg.add(sand)

                if gamemap[i][j] == '1':
                    lava= Lava(lavaim, pos)
                    lavag.add(lava)
                    scrollg.add(lava)

                if gamemap[i][j] == '2':
                    rock = Rock(rockim, pos)
                    rockg.add(rock)
                    scrollg.add(rock)

                if gamemap[i][j] == '5':
                    rcrystal = Crystal(rcrystalim, pos)
                    rcrystalg.add(rcrystal)
                    scrollg.add(rcrystal)

                if gamemap[i][j] == '6':
                    bcrystal = Crystal(bcrystalim, pos)
                    bcrystalg.add(bcrystal)
                    scrollg.add(bcrystal)


restart()
drawmap('game_lvl/rpg1.csv')
scrollg.add(player)

while True:
    dt=clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
    window.fill(black)
    gamelvl()
