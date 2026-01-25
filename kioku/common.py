import sys
import os
import random

# Constants
MAX_IN_TEST = 20

# Logic
def convert_into_line(card):
  return f"{card['front']} : {card['back']} : {card['negs']} : {card['score']}"

def convert_into_card(line):
  line = line.replace("：", ":").replace("；", ";") # Replace JP chars.
  fields = line.split(":")

  front = fields[0].strip()
  back = fields[1].strip()

  negs = 0
  score = 0

  if len(fields) == 3:
    negs = 0
    score = int(fields[2].strip())
  elif len(fields) == 4:
    negs = int(fields[2].strip())
    score = int(fields[3].strip())

  return {
    "front": front,
    "back": back,
    "negs": negs,
    "score": score
  }

# Read all lines and convert them into cards.
def read_deck_from_path(deck_path):
  cards = []

  if not os.path.exists(deck_path):
    with open(deck_path, "w"):
      pass

  with open(deck_path, "r") as f:
    for line in f:
      cards.append(convert_into_card(line))

  return cards

def write_deck_to_path(deck_path, deck):
  with open(deck_path, "w") as f:
    for card in deck:
      print(convert_into_line(card), file=f)

def get_sorted_scores(deck):
  scores = [card["score"] for card in deck]
  scores = list(set(scores))
  scores.sort()

  return scores

def get_test_cards(deck):
  # Get a list of scores, ordered from worst to best.
  scores = get_sorted_scores(deck)
  deck = random.sample(deck, len(deck))
  test_deck = []

  for score in scores:
    for card in deck:
      if card["score"] == score:
        test_deck.append(card)

      if len(test_deck) == MAX_IN_TEST:
        return test_deck

  # This handles cases when the deck is smaller than MAX_IN_TEST
  return test_deck

def reset_cards(deck):
  min_score = get_sorted_scores(deck)[0]
  for card in deck:
    card["score"] = card["score"] - min_score

def get_deck_path():
  if len(sys.argv) < 2:
    print("Please provide path to deck.")
    sys.exit()
  else:
    return sys.argv[1]
