# imports python modules required to run program and data from the current working directory (cdw) 
import pygame
import os

# screen size / max frames per second
WIDTH = 1200
HEIGHT = 700
FPS = 60
ERRORTIME = 4 # in seconds

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
CAB_GREEN = (0, 155, 0)
LIGHT_GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
DARK_RED = (100, 0, 0)

# initializes the pygame module
pygame.init()

# loads in assets from 'Assets' directory
clickerIMG = pygame.image.load(os.path.join('Assets', 'Cabbage.jfif'))

# creates window / window name / window icon / loading clock for measuring tick speed (FPS)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cabbage Clicker")
pygame.display.set_icon(clickerIMG)
clock = pygame.time.Clock()

# starting cabbages / starting autos
cabbage = 0
firAuto = 0
secAuto = 0
thrAuto = 0

# automated outputs / cabbages per second
auto1Ouput = 2
auto2Output = 60
auto3Output = 600

# sprite positions
cabbagePos = pygame.draw.rect(WIN, BLACK, pygame.Rect(400, 150, 400, 425))
sicklePos = pygame.draw.rect(WIN, BLACK, pygame.Rect(65, 335, 280, 31))
farmerPos = pygame.draw.rect(WIN, BLACK, pygame.Rect(835, 335, 280, 31))
robotPos = pygame.draw.rect(WIN, BLACK, pygame.Rect(835, 255, 280, 31))
wizardPos = pygame.draw.rect(WIN, BLACK, pygame.Rect(835, 185, 300, 31))

# farmer
def auto1():
    global cabbage
    cabbage += (firAuto * (auto1Ouput/FPS))

# robot
def auto2():
    global cabbage
    cabbage += (secAuto * (auto2Output/FPS))

# wizard
def auto3():
    global cabbage
    cabbage += (thrAuto * (auto3Output/FPS))

# template for adding text to the screen
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    WIN.blit(text, textRect)

# main game loop
def main():
    priceError = False
    harvestPower = 1
    global cabbage
    global firAuto
    global secAuto
    global thrAuto
    sickleCost = 75
    auto1Cost = 150
    auto2Cost = 2000
    auto3Cost = 50000

    run = True
    while run:
        
        WIN.fill(WHITE)
        clock.tick(FPS)
        
        auto1()
        auto2()
        auto3()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # cabbage is clicked
                if pygame.mouse.get_pressed()[0] and cabbagePos.collidepoint(pygame.mouse.get_pos()):
                    cabbage += harvestPower
                    # upgrade sickle
                if pygame.mouse.get_pressed()[0] and sicklePos.collidepoint(pygame.mouse.get_pos()):
                    if cabbage >= sickleCost:
                        cabbage = cabbage - sickleCost
                        sickleCost *= 1.5
                        harvestPower *= 2
                        priceError = False
                    elif cabbage < sickleCost:
                        priceError = True
                        itemCost = sickleCost
                        errorLen = 0
                        
                # auto1 / farmer
                if pygame.mouse.get_pressed()[0] and farmerPos.collidepoint(pygame.mouse.get_pos()):
                    if cabbage >= auto1Cost:
                        cabbage = cabbage - auto1Cost
                        auto1Cost *= 1.5
                        firAuto += 1
                        priceError = False
                    elif cabbage < auto1Cost:
                        priceError = True
                        itemCost = auto1Cost
                        errorLen = 0

                # auto2 / robot
                if pygame.mouse.get_pressed()[0] and robotPos.collidepoint(pygame.mouse.get_pos()):
                    if cabbage >= auto2Cost:
                        cabbage = cabbage - auto2Cost
                        auto2Cost *= 1.5
                        secAuto += 1
                        priceError = False
                    elif cabbage < auto2Cost:
                        priceError = True
                        itemCost = auto2Cost
                        errorLen = 0

                # auto3 / farmer
                if pygame.mouse.get_pressed()[0] and wizardPos.collidepoint(pygame.mouse.get_pos()):
                    if cabbage >= auto3Cost:
                        cabbage = cabbage - auto3Cost
                        auto3Cost *= 1.5
                        thrAuto += 1
                        priceError = False
                    elif cabbage < auto3Cost:
                        priceError = True
                        itemCost = auto3Cost
                        errorLen = 0

        WIN.blit(clickerIMG, (375, 150))

        # main cabbage display
        DrawText(str(f'{int(cabbage)}') + " Cabbages Harvested!", WHITE, CAB_GREEN , WIDTH/2, 100, 75)
        
        # store fronts
        if sickleCost > cabbage: DrawText("Upgrade Sickle: " + str(int(sickleCost)), BLACK, GRAY, 205, 350, 30)
        elif sickleCost <= cabbage: DrawText("Upgrade Sickle: " + str(int(sickleCost)), BLACK, LIGHT_GREEN, 205, 350, 30) 
        if auto1Cost > cabbage: DrawText("Buy A Farmer: " + str(int(auto1Cost)), BLACK, GRAY, 975, 350, 30)
        elif auto1Cost <= cabbage: DrawText("Buy A Farmer: " + str(int(auto1Cost)), BLACK, LIGHT_GREEN, 975, 350, 30)
        if auto2Cost > cabbage: DrawText("Buy A Robot: " + str(int(auto2Cost)), BLACK, GRAY, 975, 270, 30)
        elif auto2Cost <= cabbage: DrawText("Buy A Robot: " + str(int(auto2Cost)), BLACK, LIGHT_GREEN, 975, 270, 30)
        if auto3Cost > cabbage: DrawText("Buy A Wizard " + str(int(auto3Cost)), BLACK, GRAY, 985, 200, 30)
        elif auto3Cost <= cabbage: DrawText("Buy A Wizard " + str(int(auto3Cost)), BLACK, LIGHT_GREEN, 985, 200, 30)
        
        # achievement markers
        DrawText(f"{int((auto1Ouput*firAuto) + (auto2Output*secAuto) + (auto3Output*thrAuto))} Cabbages Per Second", WHITE, DARK_GREEN, WIDTH/2, 650, 30)
        DrawText("Farmers: " + str(firAuto), GRAY, BLACK, 890, 385, 20)
        DrawText("Robots: " + str(secAuto), GRAY, BLACK, 890, 305, 20)
        DrawText("Wizards: " + str(thrAuto), GRAY, BLACK, 890, 235, 20)
        
        # decorative elements 
        DrawText("Created By Yona V-A. and Ismael C.", BLACK, WHITE, WIDTH/2, 40, 20)
        
        # displays error when funds are insufficient
        if priceError:
            if itemCost > cabbage and errorLen < (ERRORTIME*60):
                DrawText("YOU NEED  " + str((int(cabbage) - int(itemCost)) * -1) + " MORE CABBAGES!", DARK_RED, RED, WIDTH/2, 165, 20)
                errorLen += 1
        
        pygame.display.update()
    
    pygame.quit

# will not run unless ran directly from this file
if __name__ == "__main__":
    main()
