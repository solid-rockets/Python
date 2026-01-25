import common as c

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)

while is_running:
  front_text = input("Front: ")
  back_text = input("Back: ")

  if back_text == "!exit":
    is_running = False
  else:
    card = {}
    card["front"] = front_text
    card["back"] = back_text
    card["negs"] = 0
    card["score"] = 0
    full_deck.append(card)

c.write_deck_to_path(deck_path, full_deck)
