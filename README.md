# Apixu Python

Python library for [Apixu Weather API](https://www.apixu.com/api.aspx)

## Requirements
* [Python](https://www.python.org/downloads/) (version 2 or 3)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [Git](https://git-scm.com/downloads) (optional)

#### Windows
* Download [Python](https://www.python.org/downloads/windows/)
* Install [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) if necessary
* Download [Git](https://git-scm.com/download/win)

#### Ubuntu & Debian
```
apt update
apt install -y python python-pip git
```

#### Alpine
```
apk update --no-cache
apk add python py-pip git
```

#### CentOS
```
yum install -y epel-release
yum install -y python python-pip git
```

## Install Apixu client

Choose the version you want to install from the [releases page](https://github.com/apixu/apixu-python/releases)
or choose `master` to install the latest updates.

#### pip
```
pip install git+https://github.com/apixu/apixu-python.git@vX.X.X
```
or
```
pip install git+https://github.com/apixu/apixu-python.git@master
```
or without Git
```
pip install https://github.com/apixu/apixu-python/archive/vX.X.X.zip
```

#### Requirements file
Add to `requirements.txt`
```
git+https://github.com/apixu/apixu-python.git@vX.X.X
```
then
```
pip install -r requirements.txt
```

#### Manually
```
pip install requests setuptools
git clone https://github.com/apixu/apixu-python --branch vX.X.X --single-branch # or download repository
cd apixu-python
git checkout vX.X.X
python setup.py install
```

## Usage and integration with frameworks

See the [examples](./examples).

```
APIXUKEY=yourapikey python examples/<file>.py 
```

## Documentation

https://www.apixu.com/doc/

## Development

You can use with Docker. See [Makefile](Makefile).

Run tests:
```
make test PYVERSION=3 APIXUKEY=yourapikey
```

Enter environment:
```
make env PYVERSION=3 APIXUKEY=yourapikey
python setup.py develop
pip install -r requirements-dev.txt
pytest apixu/tests/*.py
pylint apixu
```

Run example file:
```
make run PYVERSION=3 APIXUKEY=yourapikey FILE=examples/search.py
```
