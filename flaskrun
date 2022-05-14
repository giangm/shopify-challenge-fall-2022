#!/bin/bash

# Linux script

# Install all required libraries
pip install -r requirements.txt

# Check for command line argument to assign FLASK_ENV
if [ $# -eq 0 ]
    then
        env="production"
else
    env=$1
fi

# Set app environment
export FLASK_ENV=$env
# Set flask app
export FLASK_APP=run.py

# Run flask app
python run.py
