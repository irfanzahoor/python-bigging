### Writing JSON to a file ###
import json

player1 = {"name": "carlos",
"age": 35,
"languages": ["English","Portuguese"],
"city": "Porto"
}

# open file in write mode
with open("player1.txt", "w") as json_file:
    json.dump(player1, json_file)