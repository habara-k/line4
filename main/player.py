import sys
from common import *
from random import choice

class Player:
    """ プレイヤーの抽象インターフェース
    パラメータ
    ----------------
    color : BLACK or WHITE
        プレイヤーの石の色
    """
    def __init__(self, color):
        self.color = color

    def select(self, board):
        return self.ai.select(board)

class Human(Player):
    """ 人間が手を入力する """

    def select(self, board):
        while True:
            try:
                x = input('x: ')
                y = input('y: ')
                x, y = int(x), int(y)

                z = board.lowest_space(x, y)
                pos = Position(x, y, z)

                if board.available_at(pos):
                    return pos
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass

class RandomCP(Player):
    """ ランダムに手を選ぶCP """

    def select(self, board):
        pos = choice(list(board.spaces()))
        return pos
