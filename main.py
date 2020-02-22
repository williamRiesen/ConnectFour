from game import play, set_players
from students import ana, gabe, harley, kaydence, josh, tim, WJR
from tournament import choose_players

students = [ana, gabe, harley, kaydence, josh, tim, WJR]

while True:
    player1, player2 = choose_players(students)
    set_players(player1, player2)
    play()
