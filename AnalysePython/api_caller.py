import os
from openai import OpenAI
import time
from dotenv import load_dotenv
from google.cloud import language

load_dotenv()
client = OpenAI()
path = os.getenv("BARD_API_KEY")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
google = language.LanguageServiceClient()

def confidence(category: language.ClassificationCategory) -> float:
    return category.confidence

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
  print("Call chatgpt phrase : " + phrase[0])
  response = client.moderations.create(
    input=phrase[0]
  )
  print(response)
  return (phrase[0], response, phrase[1])
#response_chatgpt = completion.choices[0].message.content

def callBard(phrasesList: list):
  i = 1
  length = len(phrasesList)
  responseList = []
  for phrase, type in phrasesList:
    print("Call bard : " + str(i) + '/' + str(length))
    document = language.Document(
        content=phrase,
        type_=language.Document.Type.PLAIN_TEXT,
    )
    response = google.moderate_text(document=document)
    categories = sorted(
      response.moderation_categories,
      key=confidence,
      reverse=True,
    )
    responseList.append((phrase, categories, type))
    i += 1
  return responseList

def callBard_once(phrase: tuple):
  print("Call bard phrase : " + phrase[0])
  document = language.Document(
      content=phrase[0],
      type_=language.Document.Type.PLAIN_TEXT,
  )
  response = google.moderate_text(document=document)
  categories = sorted(
    response.moderation_categories,
    key=confidence,
    reverse=True,
  )
  return (phrase[0], categories, phrase[1])