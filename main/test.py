from Game import *

MinimaxAI_win = 0
AlphaBetaAI_win = 0

for _ in range(1):
    winner = Game().play('4', '5')
    if winner == BLACK:
        MinimaxAI_win += 1
    elif winner == WHITE:
        AlphaBetaAI_win += 1
    winner = Game().play('5', '4')
    if winner == BLACK:
        AlphaBetaAI_win += 1
    elif winner == WHITE:
        MinimaxAI_win += 1

print('勝利数\n'
      'MinimaxAI: %d \n'
      'AlphaBetaAI: %d'
      % (MinimaxAI_win, AlphaBetaAI_win))
