### Convert from Python to JSON ###
import json

# create python dictionary
player1 = {
    "name": "carlos",
    "age": 35,
    "city": "porto"
}

# converting into JSON
x = json.dumps(player1)

# displaying output
print(x)
