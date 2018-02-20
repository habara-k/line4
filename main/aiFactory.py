import sys
from ai import *


class AIFactory:
    ai_dict = {
        '1': Human,
        '2': RandomAI,
        '3': SimpleAI,
        '4': MinimaxAI,
        '5': AlphaBetaAI}
    statement = ('プレイヤーを選択してください\n'+
                 '1: Human\n'+
                 '2: RandomAI\n'+
                 '3: SimpleAI\n'+
                 '4: MinimaxAI\n'+
                 '5: AlphaBetaAI\n')

    def make_ai():
        while True:
            try:
                key = input(AIFactory.statement)
                ai_class = AIFactory.ai_dict[key]
                ai = ai_class()
                if isinstance(ai, AI):
                    return ai
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass
