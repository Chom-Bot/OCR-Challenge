import time
import csv
header = ["Name", "Password", "Points"]
player_data = []

fwrite = open('./db.csv', 'w')


print("Welcome to the roll the dice game!")
time.sleep(1)
print("You will be asked to roll a dice, if you get an even number you gain 10 points")
time.sleep(0.2)
print("If you get an odd number you lose 5 points")


p1acc = input("Player one, Do you have an account? (y/n)")


if p1acc == "y":
    p1name = input("What is your name?")
    p1pass = input("What is your password?")
else:
    p1name = input("What is your name?")
    p1pass = input("What is your password?")
    print("Welcome " + p1name)
    player_data.append(p1name)
    player_data.append(p1pass)
round = 0

csvwriter = csv.writer(fwrite)
csvwriter.writerow(header)
csvwriter.writerow(player_data)


fwrite.close()
