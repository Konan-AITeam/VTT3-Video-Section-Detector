import json

def importJSON(path):
  f = open(path, 'rt', encoding='UTF8')
  
  json_data = json.load(f)
  
  f.close()
  
  return json_data
