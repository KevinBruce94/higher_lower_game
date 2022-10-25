import random
from game_data import data
from art import logo, vs

def format_data(account):
    """Formatteer account data naar een printbaar formaat"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Controleert of het gegeven antwoord juist is"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Print logo
print(logo)
score = 0
game_should_continue = True

while game_should_continue:
    # Geneer twee random personen
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # Vraag wie meer volgers heeft
    guess = input("Who has more followers A or B? ").lower()


    # Aantal volgers per account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Geef speler feedback
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score} ")
    else:
        game_should_continue = False
        print(f"You're wrong! Final score: {score} ")