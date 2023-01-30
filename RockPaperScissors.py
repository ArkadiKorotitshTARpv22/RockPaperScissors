#Kivi Paber Kaarid
import random

while True:
    player_choice = input("Sisestage valik (kivi paber käärid): ")
    possible_choices = ["kivi", "paber", "käärid"]
    bot_choice = random.choice(possible_choices)
    print(f"\nSa valisid {player_choice}, arvuti valis {bot_choice}.\n")

    if player_choice == bot_choice:
        print(f"Mõlemad mängijad on valitud {player_choice}, see on viik!")
    elif player_choice == "kivi":
        if bot_choice == "käärid":
            print("Kivi purustab käärid, sa võitsid!")
        else:
            print("Paberkatted kivi, sa kaotasid!")
    elif player_choice == "paber":
        if bot_choice == "kivi":
            print("Paberkatted kivi, sa võitsid!")
        else:
            print("Käärid lõikasid paberit, sa kaotasid!")
    elif player_choice == "käärid":
        if bot_choice == "paber":
            print("Käärid lõikasid paberit, sa võitsid!")
        else:
            print("Kivi purustab käärid, sa kaotasid!")
    
    replay=input("Mängu uuesti mängida? (j/e): ")
    if replay.lower() != "j":
        break