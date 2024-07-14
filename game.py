import random
while True:
    print("*-*-*-*-*-*-LET THE GAME BEGIN!-*-*-*-*-*-*-*-*")
    user_choice = input("Choose: ROCK,PAPER OR SCISSORS ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
          print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
         if computer_choice == "scissors":
            print("YAYYY!!!!...Rock beats scissors!....You WIN!")
         else:
            print("OHH NOO...Paper beats rock!....You LOSE.")
    elif user_choice == "paper":
         if computer_choice == "rock":
           print("YAYYY!!!!...Paper beats rock!....You WIN!")
         else:
           print("OHH NOO...Scissors beats paper!....You LOSE.")
    elif user_choice == "scissors":
         if computer_choice == "paper":
           print("YAYYY!!!!...Scissors beats paper!....You WIN!")
         else:
           print("OHH NOO...Rock beats scissors!....You LOSE.")
    play_again=input("DO YOU WANT TO PLAY MORE??(Y/N)")
    if play_again.upper()=="N":
        print("----GAME ENDS! THANK YOU----")
        break


