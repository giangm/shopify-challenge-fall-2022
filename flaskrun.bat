@ECHO OFF

:: Install required libraries
pip install -r requirements.txt

:: Assigning command line argument to env
if [%1]==[] (env = "production") else (env = %1)

:: Setting environment variables
set FLASK_ENV=env
set FLASK_APP=run.py

:: Running flask app
python run.py