import json

def conanFormatter(csvList):
  hateSpeechList = []
  for row in csvList:
    phrase = (row['HATE_SPEECH'], object['TARGET'])
    hateSpeechList.append(phrase)
  return hateSpeechList
      