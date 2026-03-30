### convert python objects ###
import json

print(json.dumps({"name": "carlos", "age": 35}))
print(json.dumps(["orange", "lemon"]))
print(json.dumps(("apple", "fig")))
print(json.dumps("hi there"))
print(json.dumps(55))
print(json.dumps(45.87))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
