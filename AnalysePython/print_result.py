# Print results in console
# results: ({typeOfDiscrimination: (numberOfRightAnswers: number, numberOfAnswers: number)}, aiTested: string)
def printResult(results: dict):
  for resultList, name in results:
    print('=========================')
    print(name)
    print('=========================')
    for key, result in resultList.items():
      print(key + ' : ' + str(result[0]/result[1]*100) + '% juste')