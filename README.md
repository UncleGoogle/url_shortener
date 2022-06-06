# Yet another URL shortener

_Toy DRF project for simple shortening urls API_


## Usage by example

- `curl -d '{"url":"https://www.xxx.com", "alias":"xxx"}' -H "Content-Type: application/json" -X POST http://localhost:8000/shorten/`
- `curl -H "Accept: application/json" http://localhost:8000/shorten/xxx`

```
{
    "url": "https://www.xxx.com",
    "alias": "xxx"
}
```

## Installation

Recommended Python 3.8 or higher

- `pip install -r requirements/app.txt`
- `python src/manage.py migrate`
- `python src/manage.py runserver`

## Developement

### Install app in editable state with all deps
- `pip install -r requirements/dev.txt`

### Test
- `python -m pytest`

### Add dependencies

- update setup.py
- lock dependencies according to instructions in `requirements/app.txt` and `requirements/dev.txt`

### Update dependencies

- see `pip-compile -h` for "-P and -U" flags


## TODOs

- think about more cornercases, additional input sanitization(?), add test for sql injection prevention
- optional `alias` -- API would generate link itself with some hashing algorithm
- redirect to original url -- feature in `yaus` level (django "project")
- different level tests
- add openAPI document
- setup for prod, remove tokens etc. deploy somewhere
