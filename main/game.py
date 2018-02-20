from common import *
from virtualPlayer import VirtualPlayer
from board import Board
from record import Record
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
    record : Record
        棋譜
    display : Display
        表示を担う
    """

    def __init__(self):
        self.player = VirtualPlayer()
        self.board = Board()
        self.record = Record()
        self.display = Display()

    def play(self):
        """ ゲームを1回行う """
        self.refresh()                  # 初期化
        while True:                     # ゲームが終わるまで繰り返す
            self.show_board()               # 盤面を表示
            self.put()                      # 石を落とす

            if self.ended():                # 勝敗がついていれば
                self.show_result()              # 結果を表示して
                break                           # 終了

            self.switch()                   # 手番を入れ替える



    def refresh(self):
        """ 初期化 """
        self.board.refresh()
        self.record.refresh()

    def show_board(self):
        """ 盤面の表示 """
        self.display.show(self.board)

    def put(self):
        """ 石を落とし、記録する """
        player = self.player

        color = player.color()
        pos = player.select(self.board)
        self.board.put_at(pos, color)

        self.record.write(pos, color)

    def ended(self):
        """ ゲームが終わったかどうかの判定 """
        winner = self.won()
        return (self.full() or
                winner == WHITE or
                winner == BLACK)

    def show_result(self):
        """ 終了処理 """
        self.display.show(self.board)

        if self.won() == BLACK:
            self.display.won(BLACK)
        elif self.won() == WHITE:
            self.display.won(WHITE)
        elif self.board.full():
            self.display.draw()
        else:
            raise Exception

    def full(self):
        return self.board.full()

    def won(self):
        """ 勝者を返す """
        pos, color = self.record.last()
        if self.board.bingo_at(pos):
            return color
        else:
            None

    def switch(self):
        """ 手番を入れ替える """
        self.player.switch()


if __name__ == '__main__':
    Game().play()
