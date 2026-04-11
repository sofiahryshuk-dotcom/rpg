import os
import pygame
def load_image(directory):
    imgl=[]
    files=os.listdir(directory)
    for file in files:
        image=pygame.image.load(f'{directory}/{file}').convert_alpha()
        imgl.append(image)
    return imgl