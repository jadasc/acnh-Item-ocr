# Backend API for ACNH Item OCR

## Setup

Check your python version:

```
python --version
```

If the version of python is 3.6+, then great! Otherwise download python 3.6+.

Create a new virtual environment:

```
python -m venv venv
```

Activate the new python virtual environment:

```
.venv/scripts/activate
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
