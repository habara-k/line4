from common import *


class Board:
    """ 立体四目盤の実装クラス """
    STONE = {BLACK: 'x',
             WHITE: 'o',
             SPACE: '.'}

    def __init__(self):
        self.box = [[[SPACE for x in AXIS] for y in AXIS] for z in AXIS]

    def put(self, x, y, color):
        z = self.lowest_space(x, y)
        self.box[z][y][x] = color

    def put_at(self, pos, color):
        """ posにcolorの石を入れる """
        x, y, z = pos.to_xyz()
        assert z == self.lowest_space(x, y)
        self.box[z][y][x] = color

        return self.bingo_at(pos)

    def remove_at(self, pos):
        """ posにある石を取り除く """
        x, y, z = pos.to_xyz()
        self.box[z][y][x] = SPACE

    def spaces(self):
        """ 置ける座標のgenerator """
        for y in AXIS:
            for x in AXIS:
                for z in AXIS:
                    pos = Position(x, y, z)
                    if self.available_at(pos):
                        yield pos

    def filled(self):
        """ 置けない座標のgenerator """
        for y in AXIS:
            for x in AXIS:
                for z in AXIS:
                    pos = Position(x, y, z)
                    if not self.available_at(pos):
                        yield pos

    def is_full(self):
        """ 盤面が全て埋まっているかどうかの判定 """
        return not any(self.spaces())


    def bingo_at(self, pos):
        """ posを通るラインのいずれかが、4つ揃っているかどうかの判定 """
        x, y, z = pos.to_xyz()
        return any(
               all(self.box[c][b][a] == BLACK for a, b, c in line) or
               all(self.box[c][b][a] == WHITE for a, b, c in line)
               for line in lines_at[x, y, z])

    def refresh(self):
        self.box = [[[SPACE for x in AXIS] for y in AXIS] for z in AXIS]

    def show(self):
        stone = self.STONE
        for z in AXIS[::-1]:
            print('z:', z, 'x:', ' '.join(map(str, AXIS)))
            for y in AXIS:
                print('   y:', y, ' '.join(stone[x] for x in self.box[z][y]))


    def available_at(self, pos):
        """ posに置けるかどうかの判定 """
        x, y, z = pos.to_xyz()
        return self.lowest_space(x, y) == z

    def lowest_space(self, x, y):
        """ 縦のライン(x, y)における、最も低いSPACEがあるz座標 """
        for z in AXIS:
            if self.box[z][y][x] == SPACE:
                return z
        return None
