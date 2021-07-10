import pygame
import sys


class Text:
    def tetrisText():
            


            font = pygame.font.Font('Third Party Files/BebasNeue-Regular.ttf',32)
            text = font.render("Tetris",True, for i in GameVars.colers)
            GameVars.screen.blit(text,(300,50))
        



class GameVars:
    # stages in game (main menu, end screen, actual Game)
    startScreen = True
    Game = False
    endScreen = False
    running = True
    # init
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # Game objects
    playButton = pygame.Rect(250, 250, 20, 20)
    # Technical coords
    CubeX = 250
    CubeY = 250
    # Technical game vars
    colers = [(255,0,0),(0,255,0),(0,255,255)]

class Gameloop:

    def draw_grid():
        block_size = 25
        for y in range(20):
            for x in range(10):
                rect = pygame.Rect(x * block_size + 300, y * block_size + 95, block_size, block_size)
                pygame.draw.rect(GameVars.screen, (255, 255, 255), rect, 1)

    def otherGUI():
        GameVars.screen.fill((0, 0, 0))


class Mainmenu:

    def startScreen():
        GameVars.screen.fill((95, 158, 160))
        pygame.draw.rect(GameVars.screen, (0, 0, 0), GameVars.playButton)
        Text.tetrisText()
    def eventHandler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameVars.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if GameVars.playButton.collidepoint(mousePosition):
                    GameVars.startScreen = False
                    GameVars.Game = True
                    Gameloop.otherGUI()
                    Gameloop.draw_grid()

            if GameVars.startScreen == True:
                Mainmenu.startScreen()

            if GameVars.Game == True:
                Gameloop.draw_grid()

    def mainLoop():
        while GameVars.running:
            Mainmenu.eventHandler()
            pygame.display.flip()


Mainmenu.mainLoop()
