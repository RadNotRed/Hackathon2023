import os
import random
import time

# apollo 14
# found on google fr ong !!!
phrases = [
    "Fast fashion has created a massive waste problem.",
    "I flew down the hallways, barely above the ground, navigating around corners.",
    "Listen. Just because you have psychic powers doesn't make you any less human.",
    "To make bread or love, to dig in the earth, to feed an animal or cook for a stranger.",
    "Life is something that has existed for the past three to four billion years."
]

player_scores = {}

player_name_inputted_by_user = input("What is your name? ")

print("Welcome to the typing game! You will be given a phrase to type, and you will be timed.\n "
      "You will also be given a score based on how many errors you make.\n "
      "The goal is to type the phrase as fast as possible with as few errors as possible.\n "
      "Good luck!")


def test(player_name, phrase):
    os.system('cls' if os.name == 'nt' else 'clear')

    start_time = time.time()

    print("Type this phrase: {} ".format(phrase))
    user_input = input("Type here: ")

    end_time = time.time()
    total_time = end_time - start_time

    errors = 0
    for i in range(min(len(phrase), len(user_input))):
        if phrase[i] != user_input[i]:
            errors += 1

    if player_name in player_scores:
        player_scores[player_name].append((total_time, errors))
    else:
        player_scores[player_name] = [(total_time, errors)]

    print("Your score is: {} seconds and {} errors".format(total_time, errors))


players = [player_name_inputted_by_user]
for phrase in phrases:
    random.shuffle(players)
    for player in players:
        test(player, phrase)

for player, scores in player_scores.items():
    sorted_scores = sorted(scores, key=lambda x: (x[0], x[1]))
    top_scores = sorted_scores[:3]
    print("Top scores for {}".format(player))
    for i, scores in enumerate(top_scores):
        print("{}. Time: {:.2f} seconds, Errors: {}".format(i + 1, scores[0], scores[1]))
