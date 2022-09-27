import random
from unicodedata import numeric

class Hangman() :
    """
    The class Hangman() contains all the usefull functions (1 constructors and 4 functions) and statics attributes (1 attribute) 
    in order to play a hangman game.
    """
    possible_words : list[str] = ["becode", "learning", "mathematics", "sessions"]
    hangman_pictures : list[str] = ["""

                                          
                                          
                                         
                                          
                                        
                                                 
                                       """,
                                    """

                                          
                                          
                                         
                                          
                                        
                                      ============
                                       """,
                                    """

                                        |   
                                        |   
                                        |  
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   
                                        |   
                                        |  
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   
                                        |  
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |  
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |   |
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |  /|
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |  /|\\
                                        |  
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |  /|\\
                                        |  / 
                                        |
                                      ============
                                       """,
                                    """
                                       _________
                                        |   |
                                        |   O
                                        |  /|\\
                                        |  / \\
                                        |
                                      ============
                                       """]


    def __init__ (self,lives : int = 5) -> None :
        """
        The constructor(lives) function sets up all the dynamics attributes (as define the word to guess) in order to make the game ready
        it got 1 parameter to specified lives / difficulty (default at 5)
        """
        self.word_to_find : list[str] = []
        self.correctly_guessed_letters : list[str] = []
        self.wrongly_guessed_letters : list[str] = []
        self.max_lives : int = lives
        self.lives : int = self.max_lives
        self.turn_count : int = 0
        self.error_count : int = 0
        self.random_word : str = random.choice(self.possible_words)

        for letter in self.random_word :
            self.word_to_find.append(letter)
            self.correctly_guessed_letters.append("_")


    def start_game(self) -> None :
        """
        the start_game() function manages the game cycle : it lets the player guess letters trought the play() fucntion 
        and it ends up the game with the game_over() or well_played() functions.
        """
        while self.lives > 0 and "_" in self.correctly_guessed_letters :
            text_correctly_guessed_letters = ""
        
            for character in self.correctly_guessed_letters :
                text_correctly_guessed_letters += f" {character}"

            wrong_letters = " ".join(self.wrongly_guessed_letters)
            print(self.hangman_pictures[(-1*(self.lives+1))])
            print(f"Wrong letters tried : {wrong_letters}")
            print(f"Word to guess :{text_correctly_guessed_letters}, turn : {self.turn_count+1}, error : {self.error_count} (max errors = {self.max_lives}).")
            self.play()

        if self.lives == 0 :
            self.game_over()
        else :
            self.well_played()


    def play(self) -> None :
        """
        the play() function requests new letter input from the player and, based on the input correctness, updates the player status and attributes.
        """
        insert = input("Insert a new letter and try to save a man!").lower()
        while len(insert) != 1 or insert.isnumeric() == True or insert in self.correctly_guessed_letters or insert in self.wrongly_guessed_letters :
            insert = input("Insert a NEW LETTER and try to save a man! ... Even a stone can do that.").lower()
        
        if insert in self.word_to_find :
            self.correctly_guessed_letters = [character if self.word_to_find[index] != insert else insert for index , character in enumerate(self.correctly_guessed_letters)]
        else :
            self.wrongly_guessed_letters.append(insert)
            self.error_count += 1
            self.lives -= 1

        self.turn_count += 1


    def game_over(self) -> None :
        """
        the game_over() function informs the player that the game is lost.
        """
        print(self.hangman_pictures[-1])
        print("game over ...")


    def well_played(self) -> None :
        """
        the well_played() function congratulates the player and give him a feedback on the game.
        """
        word = "".join(self.word_to_find)
        print(f"You found the word: {word} in {self.turn_count} turns with {self.error_count} errors! You save a man!")