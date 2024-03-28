# Kevin Ying
import pygame
import random
from block import Block

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30
score = 0
high_score = 0

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

def create_grid(locked_pos={}):  # *
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid


def draw_text(surface, text, x, y, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (x - label.get_width()/2, y - label.get_height()/2))




def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))


def draw_window(surface, grid):
    global score, high_score
    surface.fill((0, 0, 0))

    draw_grid(surface, grid)


def main(win):
    global score, high_score
    run = True
    locked_positions = {}
    grid = create_grid(locked_positions)

    while run:
        grid = create_grid(locked_positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

        draw_window(win, grid)
        pygame.display.update()


def main_menu(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text(win, 'Welcome to Tetris',top_left_x + play_width/2, top_left_y + play_height/3, 60, (255,255,255))
        draw_text(win, 'Press Any Key To Play',top_left_x + play_width/2, top_left_y + 2 * play_height/3, 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)

