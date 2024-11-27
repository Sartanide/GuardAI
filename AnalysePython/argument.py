import sys;

# Initialisation of parameters and insertion of argument if given in parameters
def getArguments ():
  filename = "result"
  aiList = ['google', 'chatgpt']
  save_path = ""
  dataset = "./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv"
  useInterface = True
  argList: list[str] = sys.argv
  for key in range(1, len(argList)):
    match argList[key]:
      case '--filename':
        if (key < len(argList)):
          filename = argList[key + 1]
      case '--ai':
        if (key < len(argList)):
          aiList = argList[key + 1].split(',')
      case '--save_path':
        if (key < len(argList)):
          save_path = argList[key + 1]
      case '--dataset':
        if (key < len(argList)):
          dataset = argList[key + 1]
      case '--no-interface':
        useInterface = False
  return (filename, aiList, save_path, dataset, useInterface)