from aiFactory import AIFactory
from player import *
from ai import *


class PlayerFactory:
    """ プレイヤーの作成クラス """

    def make_player(color):
        ai = AIFactory.make_ai()
        player = Player(ai, color)
        return player
