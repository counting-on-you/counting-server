# Counting On You Server

This repo houses the code that is served on the Raspberry Pi that uploads data to firebase

# Installation

You are required to have `Python 3.X` and `pip` installed

First and foremost

```ssh
pip install -r requirements.txt
```

Then you run with

```ssh
python upload.py
```

To use the fake data generator

```ssh
python .\fake_data.py | python .\upload.py
```



