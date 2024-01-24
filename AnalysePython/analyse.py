

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
      