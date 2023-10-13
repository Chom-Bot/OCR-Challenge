# Get player names and passwords
player1 = input("Enter player 1 name: ")
password1 = input("Enter player 1 password: ")
player2 = input("Enter player 2 name: ")
password2 = input("Enter player 2 password: ")

if password1 != "password1" or password2 != "password2":
    print("Incorrect password. Exiting game.")
    quit()

# Play game
scores = {player1: 0, player2: 0}
for round in range(1, 6):
    print(f"Round {round}:")
    for player in [player1, player2]:
        input(f"{player}, press Enter to roll the dice.")
        score = roll_dice() + roll_dice()
        scores[player] += score
        print(f"{player} scored {score} points. Total score: {scores[player]}")

# Determine winner
if scores[player1] > scores[player2]:
    winner = player1
elif scores[player2] > scores[player1]:
    winner = player2
else:
    # Tiebreaker
    input("Tiebreaker! Press Enter to roll one die each.")
    scores[player1] += roll_dice()
    scores[player2] += roll_dice()
    if scores[player1] > scores[player2]:
        winner = player1
    else:
        winner = player2

# Print winner and scores
print(f"{winner} wins with a score of {scores[winner]}!")
