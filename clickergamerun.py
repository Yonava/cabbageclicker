import pygame
import os

pygame.init()

clickerIMG = pygame.image.load(os.path.join('Assets', 'Cabbage.jfif'))
 
WIDTH, HEIGH = 1200, 700
FULLSCREEN = (1920, 1080)
WIN = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption("Cabbage Clicker")
pygame.display.set_icon(clickerIMG)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CABBAGE_COLOR = (0, 155, 0)
GRAY = (200, 200, 200)
FPS = 60
cabbage = 0
farmers = 0

def auto1():
    global cabbage
    cabbage += (farmers / 30)

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    WIN.blit(text, textRect)

def main():
    clock = pygame.time.Clock()
    harvestPower = 1
    global cabbage
    global farmers
    sickle_cost = 75
    auto1_cost = 150

    run = True
    while run:
        auto1()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if mousePos >= (400, 0):
                    if mousePos <= (800, 0):
                        cabbage += harvestPower
                # upgrade sickle
                if mousePos >= (205, 0):
                    if mousePos <= (350, 0):
                        if cabbage >= sickle_cost:
                            cabbage = cabbage - sickle_cost
                            sickle_cost *= 1.5
                            harvestPower *= 2
                # auto1 / slave
                if mousePos >= (850, 0):
                    if mousePos <= (1100, 0):
                        if cabbage >= auto1_cost:
                            cabbage = cabbage - auto1_cost
                            auto1_cost *= 1.5
                            farmers += 1
            
        WIN.fill(WHITE)
        WIN.blit(clickerIMG, (375, 150))
        
        
        DrawText(str(f'{int(cabbage)}') + " Cabbages Harvested!", WHITE, CABBAGE_COLOR, 650, 100, 75)
        DrawText("Upgrade Sickle: " + str(int(sickle_cost)), BLACK, GRAY, 205, 350, 30)
        DrawText("Buy A Farmer: " + str(int(auto1_cost)), BLACK, GRAY, 975, 350, 30)
        DrawText("Cabbage Clicker By Yona V-A. and Ismael C.", BLACK, WHITE, 600, 10, 20)
        DrawText("Farm Workers: " + str(farmers), GRAY, BLACK, 920, 375, 20)
         
        
        
        
        
        pygame.display.update()
    

    pygame.quit


if __name__ == "__main__":
    main()
