from common import *
from playerFactory import PlayerFactory
from board import Board
from display import Display


class Game:
    """
    立体四目の実装クラス

    属性
    ------------
    board : Board
        立体四目盤
    player : VirtualPlayer
        プレイヤー
    display : Display
        表示を担う
    """

    def __init__(self):
        self.player1 = PlayerFactory.make_player(BLACK)
        self.player2 = PlayerFactory.make_player(WHITE)
        self.turn = {self.player1: self.player2,
                     self.player2: self.player1}
        self.player = self.player1

        self.board = Board()
        self.display = Display()

    def play(self):
        """ 1ゲーム行う """
        # 初期化
        self.board.refresh()

        while True:                     # ゲームが終わるまで繰り返す
            self.display.show(self.board)   # 盤面を表示

            winner = self.__put()            # 石を落とす
            if winner:
                self.__show_result(winner)

            if self.board.is_full():
                self.__show_result(None)        # 結果を表示して
                break                           # 終了

            self.player = self.turn[self.player]    # 手番を入れ替える



    def __put(self):
        """ 石を落とし、記録する """

        color = self.player.color
        pos = self.player.select(self.board)
        return self.board.put_at(pos, color)

    def __show_result(self, winner):
        """ 終了処理 """
        self.display.show(self.board)

        if winner:
            self.display.won(winner)
        else:
            self.display.draw()


if __name__ == '__main__':
    Game().play()
