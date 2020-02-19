from game import choose_players, play_game
from students import ana, gabe, harley, kaydence, josh, tim, WJR

students = [ana, gabe, harley, kaydence, josh, tim, WJR]
player1, player2 = choose_players(students)
winner = play_game(player1, player2)
print(winner.name)
