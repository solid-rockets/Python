import common as c

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)

while is_running:
  test_deck = c.get_test_cards(full_deck)

  for card in test_deck:
    input(card["front"])
    key = input(card["back"] + " ")

    match(key):
      case("y"):
        card["score"] += 1
      case("n"):
        card["score"] -= 1
      case _:
        is_running = False
        break
  c.reset_cards(full_deck)

c.write_deck_to_path(deck_path, full_deck)
