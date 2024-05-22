# import for files
import api_caller;
import get_file;
import analyse
import print_result
import save_data
# import for librairy
import sys;


def main(conanSrc):
  csvData = get_file.getCsvFile(conanSrc)
  
  # get result
  responsesGoogle = api_caller.callBard(csvData)
  responsesChatgpt = api_caller.callChatGPT(csvData)
  
  # analyse results
  results = []
  results.append((analyse.analyseGoogle(responsesGoogle), "google"))
  results.append((analyse.analyseChatGPT(responsesChatgpt), "chatgpt"))
  
  # create a render based on results
  print_result.printResult(results)
  save_data.saveDataCsv(results)

  
  
# start main
main(sys.argv[1])
