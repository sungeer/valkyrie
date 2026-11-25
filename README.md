# valkyrie

*An api built with Starlette.*

## Installation

clone:
```
$ git clone git@github.com:sungeer/valkyrie.git
$ cd valkyrie
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
then run:
```
$ uvicorn valkyrie:app --port 8848 --no-access-log
* Running on http://127.0.0.1:8848/
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
