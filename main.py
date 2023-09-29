#Author - Prashanth G

from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)


def random_number():
  randno = random.randint(0, len(data))
  return data[randno]


def printing_details(dat1, dat2):
  print(
      f"Compare A: {dat1['name']}, a {dat1['description']}, from {dat1['country']}."
  )
  print(vs)
  print(
      f"Against B: {dat2['name']}, a {dat2['description']}, from {dat2['country']}."
  )


def compare(data1, data2):
  return data1['follower_count'] >= data2['follower_count']


def play_game():
  data1 = random_number()
  data2 = random_number()
  printing_details(data1, data2)
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  if user_answer == 'A':
    return compare(data1, data2)
  else:
    return compare(data2, data1)


score = 0
result = True
while result:
  result = play_game()
  if result:
    score += 1
    clear()
    print(f"You're right! Current score: {score}")
else:
  clear()
  print(f"Sorry that's wrong, Final score: {score}")
