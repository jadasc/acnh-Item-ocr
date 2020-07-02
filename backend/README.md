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
.[virtual_environment_folder_name]/Scripts/activate
```

E.g.

> `.venv/Scripts/activate`

Now that the virtual environment is setup and activated, we need to install all the requirements from the `requirements.txt` file:

```
pip install -r requirements.txt
```

## OCR Setup

We are using the `pytesseract` python module to perform OCR.

In order to run OCR you need to download and install the OCR binary for your machine from the following location:

> https://github.com/UB-Mannheim/tesseract/wiki

In order for the Tesseract exe to be found in your python files, we need to either add the exe location to your environment variables, or change the following line of code in `\backend\text_extractor.py` to point to where the exe is located:

```
pytesseract.pytesseract.tesseract_cmd = [path/to/Tesseract-OCR/tesseract.exe]
```

## Running the API

While your virtual environment is activated, run the following command:

```
python main.py
```

This will run the API programatically, and allow you to interact with it.

You can view the available endpoints and test the API via the /docs (Swagger UI) endpoint:

> `http://localhost:5000/docs`

### Sending a picture

To send a picture to the API via alternative methods other than the Swagger UI, we need to setup a few things.

The header for the request should contain the following:

```
{
    "accept": "application/json",
    "Content-Type":"multipart/form-data"
}
```

For the request content, we need to use the multipart datatype, with a single `file` (jpeg) attached.

## Testing

Currently there are no tests.

To test out the current text_extractor.py file, run the following command after activating your virtual environment:

```
python text_extractor.py
```

## Data

https://github.com/jefflomacy/villagerdb
