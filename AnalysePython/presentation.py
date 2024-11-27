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
  responses = api_caller.callChatGPT(csvData[0:200] + csvData[600:650])
  # analyse results
  results = []
  results.append((analyse.analyseChatGPT(responses),'chatgpt'))
  # create a render based on results
  print_result.printResult(results)
  save_data.saveDataCsv(results,'result-presentation.csv')

  
  
# start main
main(sys.argv[1])
