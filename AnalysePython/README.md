# GuardAI analysis system

## Pre requisite

### Python
To use this programm you will need to install python, installation : https://www.python.org/downloads/

For linux user you will also need "pip" if not installed with python.

### OpenAI access
To use openAI you will need to create a .env file and add 'OPENAI_API_KEY = [your_key]' to it

### Google Cloud access
To use natural language AI from google cloud you will need an account and access to the api. See google tutorial at : https://cloud.google.com/natural-language/docs/reference/libraries?hl=fr#windows

When this is done you just need to add the path to the file to your .env file, created previously, in 'BARD_API_KEY'. Exemple : 'BARD_API_KEY="my_path/my_file.json"'

## Install
To install you will need openai and google-cloud on venv.

This script will create venv, activate the venv and install needed librairies in it.
```
py -m venv <venv_name>
.\<venv_name>\Scripts\activate
pip install openai python-dotenv google-cloud-storage
```
## Use
To start you can use this call
```
python .\main.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv
```


To start presentation you can use this call
```
python .\presentation.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv
```


## Source
using dataset from CONAN : https://github.com/marcoguerini/CONAN
