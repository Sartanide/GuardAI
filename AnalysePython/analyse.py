# Analyse data from ChatGPT
# responseList: [{phraseSent: string, AiResponse: any, typeOfDiscrimination: string}]
# return {typeOfDiscrimination: (numberOfRightAnswers: number, numberOfAnswers: number)}
def analyseChatGPT(responseList: list):
  i = 1
  length = len(responseList)
  responseDict: dict = {}
  for phrase, response, type in responseList:
    print("analyse : " + str(i) + '/' + str(length))
    if type in responseDict :
      if response.results[0].flagged :
        responseDict[type] = (responseDict[type][0] + 1, responseDict[type][1] + 1)
      else :
        responseDict[type] = (responseDict[type][0], responseDict[type][1] + 1)
    else :
      if response.results[0].flagged :
        responseDict[type] = (1,1)
      else:
        responseDict[type] = (0,1)
    i += 1
  return responseDict
      
# Analyse data from Google
# responseList: [{phraseSent: string, AiResponse: any, typeOfDiscrimination: string}]
# return {typeOfDiscrimination: (numberOfRightAnswers: number, numberOfAnswers: number)}
def analyseGoogle(responseList: list):
  i = 1
  length = len(responseList)
  responseDict: dict = {}
  for phrase,response,type in responseList:
    print("analyse : " + str(i) + '/' + str(length))
    i += 1
    iResp = 0
    lengthResp = len(response)
    while (iResp < lengthResp and response[iResp].confidence < 0.6):
      iResp += 1
    if type in responseDict :
      responseDict[type] = (responseDict[type][0] + int(iResp < lengthResp), responseDict[type][1] + 1)
    else :
      responseDict[type] = (int(iResp < lengthResp), 1)
  return responseDict