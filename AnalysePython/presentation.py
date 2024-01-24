# import for files
import api_caller;
import test_generator;
import get_file;
import file_formatter;
import analyse
import print_result
import save_data
# import for librairy
import sys;
import json


def main(conanSrc):
  csvData = get_file.getCsvFile(conanSrc)
  # get result
  responses = api_caller.callChatGPT(csvData[0:100])
  # analyse results
  results = analyse.analyseChatGPT(responses)
  # create a render based on results
  print_result.printResult(results)
  save_data.saveDataCsv(results,'result-presentation.csv')

  
  
# start main
main(sys.argv[1])
