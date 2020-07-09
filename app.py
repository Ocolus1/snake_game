# import math
# import random
# import tkinter as tk
# import pygame
# from tkinter import messagebox


# width = 500
# rows = 20

# class cube(object):
#     rows = 20
#     w = 500
#     def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
#         self.pos = start
#         self.dirnx = 1
#         self.dirny = 0
#         self.color = color

#     def move(self, dirnx, dirny):
#         self.dirnx = dirnx
#         self.dirny = dirny
#         self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

#     def draw(self, surface, eyes=False):
#         dis = self.w // self.rows
#         i = self.pos[0]
#         j = self.pos[1]

#         pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
#         if eyes:
#             center = dis//2
#             radius = 3
#             circleMiddle = (i * dis + center - radius, j * dis + 8)
#             circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
#             pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
#             pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


# class snake(object):
#     body = []
#     turns = {}
#     def __init__(self, color, pos):
#         self.color = color
#         self.head = cube(pos)
#         self.body.append(self.head)
#         self.dirnx = 0
#         self.dirny = 1

#     def move(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()

#             keys = pygame.key.get_pressed()

#             for key in keys:
#                 if keys[pygame.K_LEFT]:
#                     self.dirnx = -1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_RIGHT]:
#                     self.dirnx = 1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_UP]:
#                     self.dirnx = 0
#                     self.dirny = -1
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_DOWN]:
#                     self.dirnx = 0
#                     self.dirny = 1
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
        
#         for i, c in enumerate(self.body):
#             p = c.pos[:]
#             if p in self.turns:
#                 turn = self.turns[p]
#                 c.move(turn[0], turn[1])
#                 if i == len(self.body)-1:
#                     self.turns.pop(p)
#             else:
#                 if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
#                 elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
#                 elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
#                 elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
#                 else: c.move(c.dirnx, c.dirny)

#     def reset(self, pos):
#         self.head = cube(pos)
#         self.body = []
#         self.body.append(self.head)
#         self.turns = {}
#         self.dirnx = 0
#         self.dirny = 1

#     def addCube(self):
#         tail = self.body[-1]
#         dx, dy = tail.dirnx, tail.dirny

#         if dx == 1 and dy == 0:
#             self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
#         elif dx == -1 and dy == 0:
#             self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
#         elif dx == 0 and dy == 1:
#             self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
#         elif dx == 0 and dy == -1:
#             self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))
            
#         self.body[-1].dirnx = dx
#         self.body[-1].dirny = dy

#     def draw(self, surface):
#         for i, c in enumerate(self.body):
#             if i == 0:
#                 c.draw(surface, True)
#             else:
#                 c.draw(surface)
    

# s = snake((255, 0, 0), (10, 10))

# def drawGrid(w, rows, surface):
#     sizeBtwn = w // rows

#     x = 0
#     y = 0
#     for l in range(rows):
#         x = x + sizeBtwn
#         y = y + sizeBtwn

#         pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
#         pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))


# def randomSnack(rows, item):
#     positions = item.body

#     while True:
#         x = random.randrange(rows)
#         y = random.randrange(rows)
#         if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
#             continue
#         else:
#             break

#     return (x,y)


# snack = cube(randomSnack(rows, s), color=(0, 255, 0))

# def redrawWindow(surface):
#     global rows, width, s, snack
#     surface.fill((0, 0, 0))
#     s.draw(surface)
#     snack.draw(surface)
#     drawGrid(width, rows, surface)
#     pygame.display.update()



# def message_box(subject, content):
#     root = tk.Tk()
#     root.attributes("-topmost", True)
#     root.withdraw()
#     messagebox.showinfo(subject, content)
#     try:
#         root.destroy()
#     except:
#         pass


# def main():
#     global width, rows, s, snack
#     width = 500
#     rows = 20
#     win = pygame.display.set_mode((width, width))
#     s = snake((255, 0, 0), (10, 10))
#     snack = cube(randomSnack(rows, s), color=(0,255,0))
#     flag = True
#     clock = pygame.time.Clock()

#     while flag:
#         pygame.time.delay(50)
#         clock.tick(10)
#         for x in range(len(s.body)):
#             if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
#                 print("Score: ", len(s.body))
#                 message_box("You Lost!", "Play again....")
#                 s.reset((10,10))
#                 break
#         s.move()
#         if s.body[0].pos == snack.pos:
#             s.addCube()
#             snack = cube(randomSnack(rows, s), color=(0, 255, 0))

#         # for x in range(len(s.body)):
#         #     if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
#         #         print("Score: ", len(s.body))
#         #         message_box("You Lost!", "Play again....")
#         #         s.reset((10,10))
#         #         break

#         redrawWindow(win)
#     pass


# main()


import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
