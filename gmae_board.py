
import pygame

def draw_grid():
    """ Drawing a 10x10 Grid """
    block_size = 60 #Size of each block
    for x in range(0, grid_width, block_size):
        for y in range(0, grid_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, white, rect, 1)


pygame.init()

global screen, white
black = (0,0,0)
white = (255, 255, 255)
grid_height, grid_width = 600, 600
screen = pygame.display.set_mode((grid_height, grid_width))
pygame.display.set_caption("My Board")

running = True

while running:
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
