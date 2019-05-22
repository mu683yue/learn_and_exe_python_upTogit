#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
面向对象版本猜数字

version:1.0
date;2019\5\22
"""
from random import randint

class Guess(object):
    def __init__(self):
        self._answer=None
        self._counter=None
        self._hint=None

    def reset(self):
        self._answer=randint(1,100)
        self._counter=0
        self._hint=None

    def guess(self,your_answer):
        self._counter+=1
        if your_answer > self._answer:
            self._hint="大了"
        elif your_answer < self._answer:
            self._hint="小了"
        else:
            self._hint="猜对了"
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint

if __name__=='__main__':
    guess=Guess()
    play_again=True
    while play_again:
        game_over=False
        guess.reset()
        while not game_over:
            your_answer=int(input("你的数字："))
            game_over=guess.guess(your_answer)
            print(guess.hint)
        if guess.counter>10:
            print("笨蛋")
        play_again = input("再玩一次？(yes|no)")=='yes'
            
