from utils.game import Hangman

"""
the main.py file launch the Hangman game, allow the player to set the difficulty and play news games."
"""

while True : 
    difficulty = input("Define yours lives / difficulty! [1 - 10] : 1 = Hardcore ; 10 = Easy ; press Enter to acess to default (set at 5)")

    while difficulty != "" and difficulty not in [str(value) for value in range(1,11)] :
        difficulty = input("Define yours lives / difficulty! [1 - 10] : 1 = Hardcore ; 10 = Easy ; press Enter to acess to default (set at 5) ...")

    if difficulty == "" :
        game = Hangman()
    else : 
        game = Hangman(int(difficulty))
    
    game.start_game()
    replay = input("Do you want to play again? [Y/N]")

    while replay != "Y" and replay != "N" :
        replay = input("Bad command. Do you want to play again? [Y/N]")

    if replay == "Y" :
        pass
    else :
        break