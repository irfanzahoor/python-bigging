### convert from JSON to Python ###

import json
# adding some JSON
player1 = '{"name":"carlos", "age": 35, "city": "porto"}'
# parse
x = json.loads(player1)
# display the output
print(x["name"])
