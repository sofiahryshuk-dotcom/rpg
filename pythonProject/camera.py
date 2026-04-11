import pygame
class Camera():
    def __init__(self,w,h,sw,sh):
        self.w=w
        self.h=h
        self.sw=sw
        self.sh=sh
        self.offset=pygame.Vector2()
    def draw(self,window,scrollg):
        for sprite in scrollg:
            window.blit(sprite.image,sprite.rect.topleft - self.offset)
    def update(self,target,window,scrollg):
        self.draw(window,scrollg)
        self.offset.x=target.rect.centerx-self.sw//2
        self.offset.y=target.rect.centery-self.sh//2
        self.offset.x=max(0,min(self.offset.x,self.w-self.sw))
        self.offset.y=max(0,min(self.offset.y,self.h-self.sh))