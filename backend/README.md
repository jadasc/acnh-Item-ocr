# Backend API for ACNH Item OCR

## Setup

Check your python version:

```
python --version
```

If the version of python is 3.6+, then great! Otherwise download python 3.6+.

Create a new virtual environment:

```
python -m venv [virtual_environment_folder_name]
```

E.g.

> `python -m venv venv`

Activate the new python virtual environment:

```
.[virtual_environment_folder_name]/scripts/activate
```

E.g.

> `.venv/scripts/activate`

Now that the virtual environment is setup and activated, we need to install all the requirements from the `requirements.txt` file:

```
pip install -r requirements.txt
```

## Data

https://github.com/jefflomacy/villagerdb

## OCR Setup

We are using the `pytesseract` python module to perform OCR.

In order to run OCR you need to download and install the OCR binary for your machine from the following location:

> https://github.com/UB-Mannheim/tesseract/wiki


In order for the Tesseract exe to be found in your python files, we need to either add the exe location to your environment variables, or change the following line of code in `\backend\text_extractor.py` to point to where the exe is located:

```
pytesseract.pytesseract.tesseract_cmd = [path/to/Tesseract-OCR/tesseract.exe]
```

E.g.

> pytesseract.pytesseract.tesseract_cmd = r"C:\Users\YOUR_NAME\AppData\Local\Tesseract-OCR\tesseract.exe"
