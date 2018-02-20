from common import *

class Display:
    """ 表示を担うクラス """

    TURN = {BLACK: "先攻",
            WHITE: "後攻"}
    STONE = {BLACK: 'x',
             WHITE: 'o'}

    def __init__(self, graphic=True):
        self.graphic = graphic

    def show(self, board):
        """ 盤面の表示 """
        if self.graphic:
            board.show()

    def won(self, color):
        """ colorの勝利画面を表示 """
        if self.graphic:
            turn = self.TURN
            stone = self.STONE
            print("%s(%s)の勝ちです" % (turn[color], stone[color]))

    def draw(self):
        """ 引き分けを表示 """
        if self.graphic:
            print('引き分けです')
