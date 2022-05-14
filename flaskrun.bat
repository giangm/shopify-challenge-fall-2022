@ECHO OFF

:: Install required libraries
pip install -r requirements.txt

:: Setting environment variables
if [%1]==[] (set FLASK_ENV=production) else (set FLASK_ENV=%1)
set FLASK_APP=run.py

:: Running flask app
python run.py