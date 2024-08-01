# Fyle Backend Challenge

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
## **Run and Build app on Docker**

### Build and access the app at http://localhost:5000
```
docker-compose up
```
### Run the commands and access the bash within the container
```
docker exec -it fyle-interview-intern-backend-web-1 bash
```
### Ctrl + C to stop and remove the container
```
docker-compose down
```
