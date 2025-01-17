import json

def get_electron(symbol):
    with open("elements.json","r") as file:
        elements = json.load(file)

    return elements[symbol]