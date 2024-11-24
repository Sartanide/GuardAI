# import for files
import api_caller;
import get_file;
import analyse;
import print_result;
import save_data;
import argument;
import interface;

def main():
  canceled = False
  (filename, aiList, save_path, dataset, useInterface) = argument.getArguments()
  if (useInterface):
    (filename, aiList, save_path, dataset, canceled) = interface.createInterface((filename, aiList, save_path, dataset))
  if (not canceled):
    start_programm(dataset, filename, aiList, save_path)
  

def start_programm(dataset, filename, aiList, save_path):
  csvData = get_file.getCsvFile(dataset)
  results = []
  
  for ai in aiList:
    match ai:
      case 'google':
        responsesGoogle = api_caller.callBard(csvData)
        results.append((analyse.analyseGoogle(responsesGoogle), "google"))
      case 'chatgpt':
        responsesChatgpt = api_caller.callChatGPT(csvData)
        results.append((analyse.analyseChatGPT(responsesChatgpt), "chatgpt"))
  
  # create a render based on results
  print_result.printResult(results)
  save_data.saveDataCsv(results, filename, save_path)
  
# start main
main()
