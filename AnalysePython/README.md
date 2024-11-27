# GuardAI Analyze application

## Install
Python is required for this application.

to install you will need openai and google-cloud on venv
```
py -m venv <venv_name>
.\<venv_name>\Scripts\activate
pip install openai python-dotenv google-cloud-storage
```

## OpenAI
to use openAI you will need to create a .env file and add 'OPENAI_API_KEY = [your_key]' to it

## Google Cloud
To use natural language AI from google cloud you will need an account and access to the api. See google tutorial at : https://cloud.google.com/natural-language/docs/reference/libraries?hl=fr#windows. You will need to add the path to the google file in the .env like so : 'BARD_API_KEY = "path_to_key"'

## Use
to start you can use this call
```
python .\main.py
```

to start presentation you can use this call
```
python .\presentation.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv
```

## Arguments
our programm accept 5 arguments :

  - "--dataset path_to_dataset" for choosing the path where the dataset is. For exemple : "--dataset ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv" will start the programm using the basic dataset

  - "--filename name_of_file" for choosing the naming of the file, it will be generated like this type-name_of_file.csv. For exemple google with filename "result" will be saved in google-result.csv

  - "--ai ai_list" for choosing wich ai to test, it is a string array with "," as the separator. For exemple "--ai google,chatgpt" will launch analyse for chatgpt and google ai.

  - "--save_path save_path" for choosing the path where to save csv file. For exemple "--save_path ./temp/" will save file in the "temp" folder.

  - "--no-interface" for not using the interface and using arguments given or the automaticly generated ones.

to start with argument you can use this call
```
python .\main.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv --filename result --ai google,chatgpt --save_path ./saved_data/ --no-interface
```

## How it works
![alt text](https://github.com/Sartanide/GuardAI/blob/main/assets/Schematic%20Analyze%20GuardAI.jpg)

## Example of interface
![alt text](https://github.com/Sartanide/GuardAI/blob/main/assets/interface.png)

## Source
using dataset from CONAN : https://github.com/marcoguerini/CONAN
