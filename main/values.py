import copy
from common import *

class Values:
    def __init__(self, board, evaluate, color):
        self.values_ = {pos: 0
                        for pos in board.spaces()}
        self.board = copy.deepcopy(board)
        self.evaluate = evaluate
        self.color = color

        self.set_values()
        print(self.values_)

    def set_values(self):
        board = self.board
        for pos in self.values_.keys():
            board.put_at(pos, self.color)
            self.set_value_of(pos)
            board.remove_at(pos)

    def set_value_of(self, pos):
        values_ = self.values_
        if self.board.won_at(pos, BLACK):
            values_[pos] = 99
        elif self.board.won_at(pos, WHITE):
            values_[pos] = -99
        else:                               # そうでないなら評価値を計算
            values_[pos] = self.evaluate(self.board)

    def get_best_pos(self):
        values_ = self.values_
        if self.color == BLACK:
            best_value = max(values_.values())
        else:
            best_value = min(values_.values())

        pos_list = [pos
                    for pos in values_.keys()
                    if values_[pos] == best_value]
        return pos_list


class MiniMaxValues:
    def __init__(self, board, minimax_loop, color, depth):
        self.max_value = -99
        self.min_value = 99
        self.board = copy.deepcopy(board)
        self.minimax_loop = minimax_loop
        self.color = color
        self.depth = depth

        self.set_values()

    def set_values(self):
        board = self.board
        for pos in board.spaces():
            board.put_at(pos, self.color)
            self.calculate_value_of(pos)
            board.remove_at(pos)

    def calculate_value_of(self, pos):
        board = self.board
        depth = self.depth
        if board.won_at(pos, BLACK):
            self.max_value = 99 - depth
        elif board.won_at(pos, WHITE):
            self.min_value = -(99 - depth)
        else:
            value_ = self.minimax_loop(board, REVERSE[self.color], depth-1)
            self.update(value_)

    def update(self, value):
        self.max_value = max(self.max_value, value)
        self.min_value = min(self.min_value, value)

    def get_best(self):
        color = self.color
        if color == BLACK:
            return self.max_value
        elif color == WHITE:
            return self.min_value


class AlphaBetaValues(MiniMaxValues):
    def __init__(self, board, alphabeta, color, depth, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.board = copy.deepcopy(board)
        self.minimax_loop = alphabeta
        self.color = color
        self.depth = depth

        self.can_skip = False
        self.set_values()

    def set_values(self):
        board = self.board
        for pos in board.spaces():
            if self.can_skip:
                break
            board.put_at(pos, self.color)
            self.calculate_value_of(pos)
            board.remove_at(pos)

    def update(self, value):
        if self.color == BLACK:
            self.alpha = max(self.alpha, value)
        else:
            self.beta = min(self.beta, value)
        if self.alpha >= self.beta:
            self.can_skip = True

    def get_best(self):
        if self.color == BLACK:     # 手番が自分なら、最大値を選択できる
            return self.alpha
        else:                       # 手番が相手なら、最小値を選択される
            return self.beta
