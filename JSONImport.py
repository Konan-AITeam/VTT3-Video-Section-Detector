import json

def importJSON(path):
  with open(path, 'rt', encoding='UTF-8') as data_file:
    data = json.load(data_file)
  
  return data
