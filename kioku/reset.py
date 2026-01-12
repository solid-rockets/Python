import common as c

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)

for card in full_deck:
  card["score"] = 0

c.write_deck_to_path(deck_path, full_deck)
