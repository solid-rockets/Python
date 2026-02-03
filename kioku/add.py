import common as c

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)
total_num = len(full_deck)

while is_running:
  full_text = input(f"{total_num}: ")

  if full_text == "!exit":
    is_running = False
  else:
    try:
      full_text = full_text.replace("：", ":").replace("；", ";")
      parts = list(map(str.strip, full_text.split(";")))

      front_text = parts[0]
      back_text = ";".join(parts[1:])

      card = {}
      card["front"] = front_text
      card["back"] = back_text
      card["negs"] = 0
      card["score"] = 0

      full_deck.append(card)
      total_num = len(full_deck)
    except Exception as e:
      print("Enter both front and back separated by a semicolon")
      print("problem ; definition")


c.write_deck_to_path(deck_path, full_deck)
