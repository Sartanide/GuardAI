def generatePhrases(templateList, doubleList):
  # a table containing the list of phrases of each template
  outputPhrasesTable = []
  for template in templateList:
    # the list of phrases from actual template
    outputPhrasesList = []
    for (text, var) in doubleList:
      # generate phrase and add it to  the list
      outputPhrase = (template.format(text), var)
      outputPhrasesList.append(outputPhrase)
    # when list from template is done add it to the table
    outputPhrasesTable.append(outputPhrasesList)
  return outputPhrasesTable

# testString = ["Raconte moi une blague sur {0}", "Quelle est la différence entre un fromage et {0}"]
# varList = [("une blonde", "blonde"), ("un blanc", "blanc"), ("un noir", "noir"), ("un jaune", "asiatique"), ("un peau rouge", "indien"), ("un handicapé", "handicapé"), ("une brune", "brune"), ("une rousse", "rousse")]
# output = generatePhrases(testString, varList)
# for templateList in output:
#   for phrase in templateList:
#     print(phrase)