from common import *

class Player:
    """ プレイヤーの実装クラス
    パラメータ
    ----------------
    ai : AI
        手を選ぶ知能
    color : BLACK or WHITE
        プレイヤーの石の色
    """
    def __init__(self, ai, color):
        ai.set_color(color)
        self.ai = ai
        self.color = color

    def select(self, board):
        return self.ai.select(board)
