import pygame
import time
import random

pygame.init()

# Constants
color_white = (255, 255, 255)
color_blue = (0, 0, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_yellow = (255, 255, 102)
color_green = (0, 255, 0)

screen_width = 800
screen_height = 600

snake_block = 10
snake_speed = 30


screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.update()
pygame.display.set_caption('Snake Game')

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()

def show_score(score):
    display_score = score_font.render("Your Score: " + str(score), True, color_blue)
    screen.blit(display_score, [0, 0])


def move_snake(snake_block, snake_list):
    for position in snake_list:
        pygame.draw.rect(screen, color_black, [position[0], position[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/3, screen_height/3])


def game_loop():
    game_over = False
    game_close = False
    
    position_x = screen_width / 2
    position_y = screen_height / 2    

    movement_x = 0
    movement_y = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(color_white)
            message("You Lost! Press Q-Quit or C-Play Again", color_red)
            show_score(snake_length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movement_x = 0
                    movement_y = -snake_block
                if event.key == pygame.K_RIGHT:
                    movement_x = snake_block
                    movement_y = 0
                if event.key == pygame.K_DOWN:
                    movement_x = 0
                    movement_y = snake_block
                if event.key == pygame.K_LEFT:
                    movement_x = -snake_block
                    movement_y = 0

        if position_x >= screen_width or position_x < 0 or position_y >= screen_height or position_y < 0:
            game_close = True

        position_x += movement_x
        position_y += movement_y
        
        screen.fill(color_white)
        pygame.draw.rect(screen, color_green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(position_x)
        snake_head.append(position_y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        move_snake(snake_block, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if position_x == food_x and position_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
