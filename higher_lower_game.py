import random
from art import logo, vs
from game_data import data

wanna_play = True

#Print logo
print(logo)
score = 0

while wanna_play:
    # Kies twee random personen
    random_a = random.choice(data)
    random_b = random.choice(data)
    if random_a == random_b:
        random_b = random.choice(data)

    # Print beide personen
    print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.")
    print(vs)
    print(f"Compare B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")

    # Verander dictionary naar string en hiervan nemen we een key + value
    followers_a = random_a['follower_count']
    followers_b = random_b['follower_count']


    #Vraag Higher or Lower
    question = input("Who has more followers? Type 'A' or 'B': ")

    #Score vergelijken
    if question == "A".lower():
        if followers_a > followers_b:
            score += 1
            print(f"You're right! Current score: {score}.")
        elif followers_a < followers_b:
            print(f"Wrong answer. Final score: {score}")
            wanna_play = False

    elif question == "B".lower():
        if followers_b > followers_a:
            score += 1
            print(f"You're right! Current score: {score}.")
        elif followers_b < followers_a:
            print(f"Wrong answer. Final score: {score}")
            wanna_play = False
            if wanna_play is False:
                play_again = input("Type 'Y' to play again or 'N' to quit: ")
                if play_again == "Y":
                    wanna_play = True
                else:
                    quit()