# Backend: How To Run

## Assumptions:
* PostgreSQL Installed On Your Machine (`sudo apt-get install postgresql`)
* Python3 >= 3.6 (`sudo apt-get install python3` for Debian-based distros)
* All dependencies listed in [`requirements.txt`](requirements.txt) installed (`pip3 install -r requirements.txt`)

## To run the Flask server
```
python3 run.py [password for your local postgres account] [secret key for JWTs]
```
* If you don't know what your postgres account is, you could always do
```
psql [any local DB]
$ \du
```
* If you don't know what your postgres password is, you could always do
```
psql [any local DB]
$ ALTER USER postgres WITH PASSWORD 'somePassword';
```
Note that `postgres` is the default postgresql account

## To populate the database with all the courses from UNSW
```
python3 addCourseListToDB.py [password for your local postgres account]
```
