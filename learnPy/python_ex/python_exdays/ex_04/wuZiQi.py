#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
五子棋
version:1.0
date:2019\5\26
"""

import pygame

EMPTY = 0
BLACK = 1
WHITE = 2

black_color = [0,0,0]
white_color = [255,255,255]

class WuziqiBoard(object):
    def __init__(self):
        self.board = [[]] *15
        self.reset()

    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY]*15

    def move(self,row,col,is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def draw(self,screen):
        for index in range(1,16):
            pygame.draw.line(screen,black_color,
                             [40,40*index],[600,40*index],1)
            pygame.draw.line(screen,black_color,
                             [40*index,40],[40*index,600],1)
        pygame.draw.rect(screen,black_color,[36,36,568,568],4)
        pygame.draw.circle(screen,blac_color,[320,320],5,0)
        pygame.draw.circle(screen,black_color,[160,160],5,0)
        pygame.draw.circle(screen,black_color,[480,480],5,0)
        pygame.draw.circle(screen,black_color,[480,160],5,0)
        pygame.draw.circle(screen,black_color,[160,480],5,0)
        for row in range(len(self._board)):
        	for col in range(len(self._board[row])):
        		if self._board[row][col] != EMPTY:
        			ccolor = black_color if self._board[row][col] == BLACK else white_color
        			pos = [40*(col+1),40*(row+1)]
        			pygame.draw.circle(screen,ccolor,pos,20,0)

def main():
	board=WuziqiBoard()
	is_black=True
	pygame.init()
	pygame.display.set_caption("五子棋")
	screen = pygame.display.set([640,640])
	screen.fill([255,255,0])







            
        
