import random

def main():

    the_gang = ["rock", "paper", "scissors"]

    print("rock paper or scissors?")

    player_input = ""


    while True:
        player_input == input()
        computer_int_play = the_gang[random.randint(0,2)]
        print(computer_int_play)
        if (player_input == "rock" and computer_int_play == "scissors") or (player_input == "scissors" and computer_int_play == "paper") or (player_input == "paper" and computer_int_play == "rock"):
            print(player_input + " beat " + computer_int_play)
        elif (computer_int_play == "rock" and player_input == "scissors") or (computer_int_play == "scissors" and player_input == "paper") or (computer_int_play == "paper" and player_input == "rock"):
            print(computer_int_play + " beat " + player_input)
        else:
            print("-----draw, try again-----")
            print(player_input)
            print(computer_int_play)
            break
            
            
            
         

if __name__ == '__main__':
    main()