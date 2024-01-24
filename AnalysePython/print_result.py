def printResult(results: dict):
  for key, result in results.items():
    print(key + ' : ' + str(result[0]/result[1]*100) + '% juste')