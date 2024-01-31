
import pygame

import requests


WIDTH = 550

background_color = (251, 247, 245)

original_grid_element_color = (52, 31, 151)

buffer = 5


# little API usage

response = requests.get('https://sugoku.onrender.com/board?difficulty=easy')

grid = response.json()['board']

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]



def insert(win, position):

    i, j = position[1], position[0]

    myfont = pygame.font.SysFont('Comic Sans MS', 35)


    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if grid_original[i-1][j-1] != 0:
                    return

                if event.key == 48:

                    grad[i-1][j-1] = event.key - 48

                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+buffer), 50-buffer, 50-buffer)
                    pygame.display.update()
                jls_extract_var = 0
                if jls_extract_var < event.key-48 < 10:

                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+buffer), 50-buffer, 50-buffer)

                    value = myfont.render(str(event.key-48), True, (0, 0, 0))

                    win.blit(value, (position[0]*50 + 15, position[1]*50))

                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
        return                       



def main():
    pygame.init()

    #initializing the screen for the game

    win = pygame.display.set_mode((WIDTH, WIDTH))    

    # setting a caption, obviously... 

    pygame.display.set_caption("Sudoku")    

    # painting the background    

    win.fill(background_color)

    # setting the font for the numbers

    myfont = pygame.font.SysFont('Comic Sans MS', 35)


    for i in range(0, 10):


        # for the bold lines that separate the little boxes

        if i%3 == 0:

            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 4)

            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4)


        # for the other lines

        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)

        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
        pygame.display.update()



    for i in range(0, len(grid[0])):

        for j in range(0, len(grid[0])):

            if 0 < grid[i][j] < 10:

                # generates an image 

                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)

                # draws the image onto the screen at given position

                win.blit(value, ((j+1)*50 + 15, (i+1)*50))

        pygame.display.update()


    # this keeps the window open

    while True:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                pos = pygame.mouse.get_pos()

                insert(win, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:

                pygame.quit()
                return

main()

















