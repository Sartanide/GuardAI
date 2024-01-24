import json;
import csv;

def getFileReadlines(src):
  with open(src, 'r') as file:
    data = file.readlines()
  return data

def getFileRead(src):
  with open(src, 'r') as file:
    data = file.read()
  return data

def getJsonFile(src):
  jsonData = []
  with open(src, 'r') as jsonFile:
    jsonData = json.load(jsonFile)
  return jsonData['conan']

def getCsvFile(src):
  csvPhrases = []
  with open(src, 'r', encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
      csvPhrases.append((row[1], row[3]))
  return csvPhrases