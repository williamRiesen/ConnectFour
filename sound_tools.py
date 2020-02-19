def play_checker_drop_sound(player1, player2, current_player):
    if current_player == 1:
        player1.sound.play()
    elif current_player == 2:
        player2.sound.play()
    else:
        print("Error: current_player must be 1 or 2")