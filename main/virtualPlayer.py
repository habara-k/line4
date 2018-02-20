from common import *
from playerFactory import PlayerFactory


class VirtualPlayer:
    """ GameクラスとPlayerクラスとの仲介クラス """

    def __init__(self):
        self.player1 = PlayerFactory.make_player(BLACK)
        self.player2 = PlayerFactory.make_player(WHITE)

        self.turn = {self.player1: self.player2,
                     self.player2: self.player1}
        self.player = self.player1

    def switch(self):
        self.player = self.turn[self.player]

    def select(self, board):
        return self.player.select(board)

    def color(self):
        return self.player.color
