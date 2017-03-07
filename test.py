import json

filename = 'participants.json'
try:
    people = json.load(open(filename))
except Exception as e:
    print("Could not read {}".format(filename))
    print(e)
    exit(1)

for p in people:
    for field in ['name', 'github']:
        if field not in p:
            exit("'{}' is missing from {}".format(field, str(p)))

