import random

# global scores for a game
PlayerScore = 0
ComputerScore = 0
# available choices
choices = {"1":"Rock","2":"Paper","3":"Scissor"}
# rounds count
n = 0

# printing the instruction
def instruction():
    print("Rules for the Game:")
    print("-----------------------------")
    print("Rock Beats Scissors\nPaper Beats Rock\nScissor Beats Paper")

# printing choices available
def choicesAvailable():
    print("-----------------------------")
    print("Choices available:   ")
    print("-----------------------------")
    print("1. Rock\n2. Paper\n3. Scissor")
    print("-----------------------------")


# getting computer choice and determining the winner 
def winner(PlayerChoice):
    global n, PlayerScore, ComputerScore
    n+=1
    ComputerChoice = random.choice(["1","2","3"])
    print("Your choice: ",choices[PlayerChoice])
    print("Computer choice: ",choices[ComputerChoice])
    if ComputerChoice == PlayerChoice:
        print("This round is a tie !")
    elif ((ComputerChoice=="1" and PlayerChoice=="2") or (ComputerChoice=='2' and PlayerChoice=='3') or (ComputerChoice=='3' and PlayerChoice=='1')):
        PlayerScore+=1
        print("You win!")
    else:
        ComputerScore+=1
        print("You Lose!")

 # game where player enters his choice and result is shown   
def game():
    resume = "Y"
    while resume in "yY":
        choicesAvailable()
        PlayerChoice = input("Enter your choice (1/2/3) :")
        if PlayerChoice not in ["1","2","3"]:
            print("Enter a valid choice (1/2/3) :")
        else:
            print("-----------------------------")
            winner(PlayerChoice)
            print("Score after round",n)
            print("Player Score ->",PlayerScore)
            print("Computer Score ->",ComputerScore)
            print("-----------------------------")

            resume = input("Do you want to play again? (Y/N) ")

            if resume in "Nn":
                print("-----------------------------")
                print("Your final Score: ",PlayerScore)
                print("Computer final Score: ",ComputerScore)
                if(PlayerScore==ComputerScore):
                    print("The game is a tie!")
                elif PlayerScore>ComputerScore:
                    print("You win the Game!")
                else:
                    print("You Lose the Game!\nBetter luck next time.")
                print("-----------------------------")
            elif resume not in "YyNn":
                resume = "Y"
                print("Enter a valid choice")


instruction()
game()

