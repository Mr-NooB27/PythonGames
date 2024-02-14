import random
def get_choices():
    player_choice = input("enter a choice (rock, paper, scissor) : ")
    options = ["paper", "rock", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose  {player}, computer chose {computer}" )
    if player == computer:
         return "it's a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissor, you win"
        else:
            return "paper covers rock, you lose"
    elif player == "paper":
        if computer == "scissor":
            return "scissor cuts paper, you lose"
        else:
            return "paper covers rock, you win"
    elif player == "scissor":
        if computer == "paper":
            return "scissor cuts paper, you win" 
        else:
            return "prock smashes scissor, you lose"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
