import json

filename = 'participants.json'
try:
    json.load(open(filename))
except Exception as e:
    print("Could not read {}".format(filename))
    print(e)
    exit(1)
