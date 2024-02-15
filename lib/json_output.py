import json

def createJSON(dict):
    with open('Paragraphs.json', 'w') as fp:
        json.dump(dict, fp, indent=4)
