import random
rock="R"
paper="P"
scissors="S"

while True:
    print("Enter choice \n R for rock, \n P for paper, \n S for scissors")
    user_action=input("Enter a chioce(rock[R],paper[P],scissors[S]):")
    possible_actions=("rock","paper","scissors")
    computer_action=random.choice(possible_actions)

    if user_action=="R":
        user_action="rock"
    elif user_action=="P":
        user_action="paper"
    else:
        user_action="scissors"
    print(f"\nyou chose", {user_action},"computer chose",{computer_action})
    if user_action==computer_action:
        print(f"Both player selected",{user_action},". it's a tie!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock smashes Scissors! You Win!")
        else:
            print("Paper covers Rock! You lose.")

    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers Rock! You Win!")
        else:
            print("Scissors cuts Paper! You lose.")

    elif user_action=="scissors":
        if computer_action=="paper":
            print("Scissors cuts Paper ! You Win!")
        else:
            print("Rock smashes Scissors! You lose.")

        play_again=input("Do you want to play Again? Y/N:")
        if play_again.lower()=="n":
            print("Thanks For Playing!")
            break
        
    
    
