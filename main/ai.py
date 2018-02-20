import sys
from common import *
from values import Values, MiniMaxValues, AlphaBetaValues
from random import choice

class AI:
    """ AIの抽象インターフェース """
    def select(self, board, color):
        pass

    def set_color(self, color):
        self.color = color


class Human(AI):
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


class RandomAI(AI):
    """ ランダムに手を選ぶAI """

    def select(self, board):
        pos = choice(list(board.spaces()))
        return pos


class SimpleAI(AI):
    """ 簡単なAI """

    def select(self, board):
        values = Values(board, self.calculate, self.color)
        pos = choice(values.get_best_pos())
        return pos

    def calculate(self, board):
        """ 盤面の評価値を返す """
        return sum(
            board.box[z][y][x]
            for line in lines()
            for x, y, z in line
            if all(board.box[z][y][x] != BLACK for x, y, z in line) or
               all(board.box[z][y][x] != WHITE for x, y, z in line))




class MinimaxAI(SimpleAI):

    DEPTH = 2

    def select(self, board):
        values = Values(board, self.minimax, self.color)
        pos = choice(values.get_best_pos())
        return pos
    
    def minimax(self, board):
        return self.minimax_loop(board, REVERSE[self.color], depth=self.DEPTH)

    def minimax_loop(self, board, color, depth):
        """ ミニマックス法 """
        if depth == 0:              # 探索限界に到達したら、評価値を計算
            return self.calculate(board)

        values = MiniMaxValues(board, self.minimax_loop, color, depth)
        return values.get_best()




class AlphaBetaAI(MinimaxAI):

    DEPTH = 2

    def minimax(self, board):
        return self.alphabeta(board, REVERSE[self.color], depth=self.DEPTH)

    def alphabeta(self, board, color, depth, alpha=-99, beta=99):
        """ アルファベータ法 """
        if depth == 0:              # 探索限界に到達したら、評価値を計算
            return self.calculate(board)

        values = AlphaBetaValues(board, self.alphabeta, color, depth, alpha, beta)
        return values.get_best()
    

