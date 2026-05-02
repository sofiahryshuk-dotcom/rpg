import sys
from sprites.sprite_classes import*
from pygwidgets import*
pygame.mixer.init()
white=(255,255,255)
w=800
h=800
FPS=60
pygame.init()
window=pygame.display.set_mode((w,h))
pygame.display.set_caption('(ˉ﹃ˉ)')
clock=pygame.time.Clock()
from camera import Camera
MINIMAPTI=5
MINIMAPPOS=(10,10)

from load import*
def restart():
    global player, playerg, sandg, waterg, lavag, grassg, rockg, scrollg, rcrystalg, bcrystalg, camera, colsp, pickg,qt,qv,npcg,qt2,qv2,cst,cs
    playerg = pygame.sprite.Group()
    cst = pygwidgets.DisplayText(window, (0, 0), 'MONEY:0', fontSize=40, textColor=(255, 0, 255))
    cs=0

    qt = DisplayText(window, (0, 0), 'ПЕРЕКРАСЬ МИР ', 'Helvetica', fontSize=30, textColor=(0, 0, 0),backgroundColor=(198, 77, 228))
    qv = False
    qt2 = DisplayText(window, (0, 0), 'дай 4 монеты-получи зеленую краску', 'Helvetica', fontSize=30, textColor=(0, 0, 0),
                     backgroundColor=(67, 42,52))
    qv2 = False
    cst.setLoc((0,0))

    sandg = pygame.sprite.Group()
    waterg = pygame.sprite.Group()
    lavag = pygame.sprite.Group()
    grassg = pygame.sprite.Group()
    rockg = pygame.sprite.Group()
    scrollg = pygame.sprite.Group()
    rcrystalg = pygame.sprite.Group()
    bcrystalg = pygame.sprite.Group()
    pickg = pygame.sprite.Group()
    npcg = pygame.sprite.Group()
    camera = Camera(8000, 8000, w, h)
    colsp = pygame.sprite.Group()
    player = Player(playerim['right'][0], (400, 400), colsp)
    playerg.add(player)

def gamelvl():
    global player, playerg, waterg, grassg, lavag, sandg, rockg, scrollg, rcrystalg, bcrystalg, camera, colsp, bcrystals, opsize, gamemap, rcrystals, pickcol, pick,qt,qv,npcg,qt2,qv2,cst,cs
    # waterg.draw(window)
    # grassg.draw(window)
    # lavag.draw(window)
    # sandg.draw(window)
    # rockg.draw(window)
    # rcrystalg.draw(window)
    # bcrystalg.draw(window)
    # playerg.draw(window)
    #upmusic()
    npcg.update( playerg, player,FPS,npcim)
    playerg.update(dt, FPS, playerim)
    camera.update(player, window, scrollg)
    cst.draw()

    if showminimap:
        drawminimap()


    rcryscol = pygame.sprite.spritecollide(player, rcrystalg, True)
    cryscol = pygame.sprite.spritecollide(player, bcrystalg, True)
    for crystal in rcryscol:
        rcrystals += 1
        cs+=1
        cst.setValue(f'MONEY:{cs}')
        i, j = crystal.tilep
        gamemap[i][j] = '3'
        player_pos = player.rect.center
        drawmap()
        player.rect.center = player_pos
        player.pos = pygame.Vector2(player_pos)
        scrollg.add(player)

    for crystal in cryscol:
        clean()
        i, j = crystal.tilep
        gamemap[i][j] = '3'
        player_pos = player.rect.center
        drawmap()
        player.rect.center = player_pos
        player.pos = pygame.Vector2(player_pos)
        scrollg.add(player)
    qv = False
    qv2=False
    for npc in npcg:
        dis = ((player.rect.centerx - npc.rect.centerx)**2+(player.rect.centery - npc.rect.centery)**2)**0.5

        if dis < 100:
            print(player.rect.centery)
            if player.rect.centery<2000:
             qv = True
             qt.setLoc((300,300))
            else:
                if rcrystals<4:
                 qv2=True
                 qt2.setLoc((300, 300))
                else:
                    clean()
                    cs=0
                    cst.setValue(f'MONEY:{cs}')

    if qv==True:
        qt.draw()
    if qv2==True:
        qt2.draw()
    pygame.display.update()






def drawminimap():
    global gamemap,showmm
    for i in range(100):
        for j in range(100):

          tile = gamemap[i][j]
          x=MINIMAPPOS[0]+j*MINIMAPTI
          y=MINIMAPPOS[1]+i*MINIMAPTI
          if tile =='0':
              color=(50,200,50)
          elif tile =='1':
              color=(240,120,50)
          elif tile =='2':
              color=(100,100,100)
          elif tile =='3':
              color=(250,215,155)
          elif tile =='4':
              color=(50,200,240)
          pygame.draw.rect(window,color,(x,y,MINIMAPTI,MINIMAPTI))
          playertix=int(player.rect.centerx//80)
          playertiy=int(player.rect.centery//80)
          px=MINIMAPPOS[0]+playertix*MINIMAPTI
          py=MINIMAPPOS[1]+playertiy*MINIMAPTI
          pygame.draw.rect(window,(255,255,255),(px,py,MINIMAPTI,MINIMAPTI))

def clean():
    global gamemap
    for i in range(100):
        for j in range(100):
            if gamemap[i][j]=='1':
                gamemap[i][j]='0'
    player_pos = player.rect.center
    drawmap()
    player.rect.center = player_pos
    player.pos = pygame.Vector2(player_pos)
    scrollg.add(player)

gamemap=[]
def loadmap(mapFile):
    global gamemap
    with open(mapFile, 'r') as file:
        for line in file:
            gamemap.append(line.replace('\n', '').split(','))
    print(len(gamemap))


def drawmap():
    global sandg,waterg,grassg,rockg,lavag,scrollg,rcrystalg,bcrystalg,camera,colsp,gamemap,opsize,pickg,qt,qv,npcg,qt2,qv2,cst,cs
    scrollg.empty()
    grassg.empty()
    sandg.empty()
    lavag.empty()
    waterg.empty()
    bcrystalg.empty()
    rcrystalg.empty()
    colsp.empty()
    rockg.empty()
    pickg.empty()
    npcg.empty()



    pos = [0, 0]
    for i in range(opsize):
        pos[1] = i * 80
        for j in range(opsize):
            pos[0] = j * 80

            if gamemap[i][j] == '0':
                grass = Grass(grassim, pos)
                grassg.add(grass)
                scrollg.add(grass)

            if gamemap[i][j] == '4':
                water = Water(waterim, pos)
                waterg.add(water)
                scrollg.add(water)
                colsp.add(water)

            if gamemap[i][j] == '3':
                sand = Sand(sandim, pos)
                sandg.add(sand)
                scrollg.add(sand)

            if gamemap[i][j] == '1':
                lava= Lava(lavaim, pos)
                lavag.add(lava)
                scrollg.add(lava)

            if gamemap[i][j] == '2':
                rock = Rock(rockim, pos,(i,j))
                rockg.add(rock)
                scrollg.add(rock)
                colsp.add(rock)

            if gamemap[i][j] == '5':
                rcrystal = Crystal(coinim, pos,(i,j))
                rcrystalg.add(rcrystal)
                scrollg.add(rcrystal)

            if gamemap[i][j] == '6':
                bcrystal = Crystal(bcrystalim, pos,(i,j))
                bcrystalg.add(bcrystal)
                scrollg.add(bcrystal)

            if gamemap[i][j] == '7':
                pick = Pick(pickim, pos, (i, j))
                pickg.add(pick)
                scrollg.add(pick)

            if gamemap[i][j] == '8':
                npc = NPC(npcim[0], pos)
                npcg.add(npc)
                scrollg.add(npc)



opsize=100
bcrystals=0
restart()
rcrystals=0
loadmap('game_lvl/mgs.csv')
drawmap()
scrollg.add(player)
showminimap=False
curzone=None

while True:


    dt=clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_m:
                showminimap=not showminimap
            if event.key ==pygame.K_SPACE:
                player.mine(gamemap)
                player_pos = player.rect.center
                drawmap()
                player.rect.center = player_pos
                player.pos = pygame.Vector2(player_pos)
                scrollg.add(player)
            if event.key==pygame.K_p:
                pygame.mixer.music.pause()
            if event.key==pygame.K_o:
                pygame.mixer.music.unpause()



    window.fill(white)
    gamelvl()