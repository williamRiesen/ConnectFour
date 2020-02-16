from Game import game_loop
from SelectPlayers import select_players

rows = 6
columns = 7

while True:
    player1, player2 = select_players()
    game_loop(rows, columns, player1, player2)
