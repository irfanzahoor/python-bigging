# parse json file
import json

with open('player.json') as f:
    data = json.load(f)

# displaying output
print(data)
