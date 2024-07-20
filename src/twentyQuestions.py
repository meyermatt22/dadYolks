import sys

class TwentyQuestionsGame:
    def __init__(self):
        self.max_questions = 20
        self.question_number = 1
        self.current_question = ""
        self.guess = None

    def start_game(self):
        print("Welcome to the 20 Questions game!")
        print("Think of an object, and I will try to guess it.")
        print("Please answer with 'yes' or 'no'.\n")

        self.ask_question()

    def ask_question(self):
        if self.question_number == 1:
            self.current_question = "Is it alive? "
        elif self.question_number == 2:
            self.current_question = "Is it bigger than a breadbox? "
        elif self.question_number == 3:
            self.current_question = "Is it man-made? "
        elif self.question_number == 4:
            self.current_question = "Is it edible? "
        elif self.question_number == 5:
            self.current_question = "Is it used indoors? "
        elif self.question_number == 6:
            self.current_question = "Is it made of metal? "
        elif self.question_number == 7:
            self.current_question = "Is it found in nature? "
        elif self.question_number == 8:
            self.current_question = "Is it related to technology? "
        elif self.question_number == 9:
            self.current_question = "Is it a form of transportation? "
        elif self.question_number == 10:
            self.current_question = "Is it smaller than a toaster? "
        elif self.question_number == 11:
            self.current_question = "Is it used for communication? "
        elif self.question_number == 12:
            self.current_question = "Is it found in the kitchen? "
        elif self.question_number == 13:
            self.current_question = "Is it found in the bathroom? "
        elif self.question_number == 14:
            self.current_question = "Is it used for entertainment? "
        elif self.question_number == 15:
            self.current_question = "Is it a piece of furniture? "
        elif self.question_number == 16:
            self.current_question = "Is it expensive? "
        elif self.question_number == 17:
            self.current_question = "Is it a tool? "
        elif self.question_number == 18:
            self.current_question = "Is it a type of clothing? "
        elif self.question_number == 19:
            self.current_question = "Is it a type of animal? "
        elif self.question_number == 20:
            self.current_question = "Is it a type of vehicle? "
        else:
            self.guess = input("I give up. What are you thinking of? ")
            return

        answer = input(f"Question {self.question_number}: {self.current_question}").lower().strip()

        if answer == 'yes':
            self.question_number += 1
            self.ask_question()
        elif answer == 'no':
            self.question_number += 1
            self.ask_question()
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            self.ask_question()

    def end_game(self):
        if self.guess:
            print(f"\nAh, I see! You were thinking of {self.guess}.")
        else:
            print("\nI couldn't guess what you were thinking of.")

        print("\nThanks for playing!")

# Run the game
game = TwentyQuestionsGame()
game.start_game()
game.end_game()
