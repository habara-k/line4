from common import *

class Record:
    def __init__(self):
        self.list = []

    def refresh(self):
        self.list = []

    def write(self, pos, color):
        """ 棋譜に残す """
        self.list.append((pos, color))

    def last(self):
        """ 一番最後に置いた座標と、その石を返す """
        return self.list[-1]
