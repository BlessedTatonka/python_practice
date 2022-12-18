import json
import pprint

with open('output.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)

print(json_data)

pprint.pprint(json_data)