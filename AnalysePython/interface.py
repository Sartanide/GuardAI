# for screen size
from tkinter import *;
from tkinter import filedialog;
from tkinter import ttk;

filename = "result"
aiList = ['google', 'chatgpt']
save_path = ""
dataset = "./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv"
interface = Tk()
canceled = True
chosenAi = []
listbox: Listbox

def getSavePath () :
  global save_path
  savePath = filedialog.askdirectory()
  if (savePath):
    save_path = savePath
  
def getDataset ():
  global dataset
  datasetFile = filedialog.askopenfilename()
  if (datasetFile):
    dataset = datasetFile

def get_size (interface):
  width = min(interface.winfo_screenwidth(), 400)
  height = min(interface.winfo_screenheight(), 400)
  return (width, height)

def confirm ():
  global interface
  global canceled
  global chosenAi
  global listbox
  canceled = False
  chosenAi = []
  choiceList = listbox.curselection()
  for i in choiceList:
    chosenAi.append(aiList[i])
  interface.destroy()

def createInterface (input = None):
  global interface
  global filename
  global aiList
  global save_path
  global dataset
  global chosenAi
  global listbox
  
  if (input):
    (filename, chosenAi, save_path, dataset) = input
  
  filenameVar = StringVar(interface, "result")

  (width, height) = get_size(interface)
  interface.geometry(str(width) + "x" + str(height))
  interface.title("GuardAi Analyser")
  interface.resizable(width=True, height=True)
  # Setting up frame for separating form in two groups
  left_frame  =  Frame(interface,  width=180,  height=  180)
  left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

  right_frame  =  Frame(interface,  width=180,  height=180)
  right_frame.grid(row=0,  column=1,  padx=10,  pady=5)
  
  bottom_left_frame = Frame(interface,  width=180,  height=180)
  bottom_left_frame.grid(row=1,  column=0,  padx=10,  pady=5)
  bottom_right_frame = Frame(interface,  width=180,  height=180)
  bottom_right_frame.grid(row=1,  column=1,  padx=10,  pady=5)
  
  # Filename part
  labelInputFilename = Label(left_frame, text="Filename for save file")
  inputFilename = Entry(left_frame, textvariable=filenameVar)
  
  # Choose dataset file button
  datasetBtn = Button(left_frame, text="Choose dataset", bg="blue", fg="white", command=getDataset)
  
  # Choose save path folder button for results
  save_pathBtn = Button(left_frame, text="Choose save directory", bg="blue", fg="white", command=getSavePath)
  
  # create a label for the combobox
  label = Label(right_frame, text="Select ai to test:")
  
  # create a Listbox widget for the dropdown list
  listbox = Listbox(right_frame, selectmode="multiple", exportselection=0, listvariable=chosenAi)
  for ai in aiList:
    listbox.insert(END, ai)
  for ai in range(len(chosenAi)):
    listbox.selection_set(ai)
  
  #Confirm button
  confirmBtn = Button(bottom_left_frame, text="Confirm", bg="green", fg="white", command=confirm)
  
  #Cancel button
  cancelBtn = Button(bottom_right_frame, text="Cancel", bg="red", fg="white", command=interface.destroy)
  
  labelInputFilename.grid(column=0, ipady=1, padx=10)
  inputFilename.grid(column=0, padx=10)
  datasetBtn.grid(column=0, pady=10, padx=10)
  save_pathBtn.grid(column=0, pady=0, padx=10)
  label.grid(column=2, padx=20, pady=0)
  listbox.grid(column=2, padx=20, pady=20)
  confirmBtn.pack(side="right", padx=10, pady=0)
  cancelBtn.pack(side="left", padx=10, pady=0)
  
  chosenAi = listbox.curselection()
  
  interface.mainloop()
  
  global canceled
  filename = filenameVar.get()
  return (filename, chosenAi, save_path, dataset, canceled)
