### Python pretty print JSON ###
import json

player = '{"name": "carlos", "age": 35, "languages": ["English", "Portuguese"], "levels": [10, 10.5, null]}'

# we can get the player dict
player_dict = json.loads(player)

# displaying JSON string with editing
print(json.dumps(player_dict, indent = 4, sort_keys = True))