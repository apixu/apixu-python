# APP

## Django app using Apixu

### Requirements
* Python 3.5+ (if other version required, adjust [requirements.txt](./requirements.txt))
* pip

### Setup app

Set SECRET_KEY and APIXUKEY in the .env file.
```
cp .env.dist .env
```

Set Apixu library dependency in [requirements.txt](./requirements.txt).

### Install dependencies
```
pip install -r requirements.txt
```

### Run app
```
python manage.py runserver
```

### Test
```
curl "127.0.0.1:8000/weather?q=London"
```
