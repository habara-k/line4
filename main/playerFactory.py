import sys
from player import *


class PlayerFactory:
    """ プレイヤーの作成クラス """
    player_dict = {
        '1': Human,
        '2': RandomCP
        }
    statement = ('プレイヤーを選択してください\n'+
                 '1: Human\n'+
                 '2: RandomAI\n'
                 )

    @classmethod
    def make_player(cls, color):
        while True:
            try:
                key = input(cls.statement)
                player_cls = cls.player_dict[key]
                player = player_cls(color)
                if isinstance(player, Player):
                    return player
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass

