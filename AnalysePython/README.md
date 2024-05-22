# Groupe de navatt_l 1010002

## Install
to install you will need openai and google-cloud on venv
```
py -m venv <venv_name>
.\<venv_name>\Scripts\activate
pip install openai python-dotenv google-cloud-storage
```
## Use
to start you can use this call
```
python .\main.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv
```


to start presentation you can use this call
```
python .\presentation.py ./CONAN-master/Multitarget-CONAN/Multitarget-CONAN.csv
```


## Source
using dataset from CONAN : https://github.com/marcoguerini/CONAN

## OpenAI
to use openAI you will need to create a .env file and add 'OPENAI_API_KEY = [your_key]' to it

## Google Cloud
To use natural language AI from google cloud you will need an account and access to the api. See google tutorial at : https://cloud.google.com/natural-language/docs/reference/libraries?hl=fr#windows