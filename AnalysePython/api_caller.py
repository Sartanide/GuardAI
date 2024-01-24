import os
from openai import OpenAI
import time
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def callChatGPT(phrasesList: list):
  i = 1
  length = len(phrasesList)
  responseList = []
  for phrase, type in phrasesList:
    print("api call : " + str(i) + '/' + str(length))
    response = client.moderations.create(
      input=phrase
    )      
    responseList.append((phrase, response, type))
    i += 1
  return responseList
#response_chatgpt = completion.choices[0].message.content

def callChatGPT_once(phrase: tuple):
  print("Phrase envoyé : " + phrase[0])
  response = client.moderations.create(
    input=phrase[0]
  )
  print(response)
  return (phrase[0], response, phrase[1])
#response_chatgpt = completion.choices[0].message.content