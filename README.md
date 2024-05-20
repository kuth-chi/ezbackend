# ezbackend
Open terminal from directory you want to place this project.

```bash
gh repo clone ez-startup/ezbackend
```
Make sure the directory is empty. 

## Create Python Virtualenv for development
Install VirtualEnv
```powershell
pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
```
To install all dependencies from requirements.txt file.
```powershell
pip install -r requirements.txt
```
Make sure you have development virtual environment is activated. 

## Create Database by Make Migrations
From you project directory in terminal by activated venv run the command line below
```shell
python manage.py makemigrations
python manage.py migrate
```
## Run Server
```shell
python manage.py runserver 0.0.0.0:8000 --open
```
Done with greate job!
Now to access your website browsing with default browser. 
