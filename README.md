# Fall 2022 - Shopify Developer Intern Challenge

An inventory tracking web application for a logistics company with CRUD and undelete features. This web application is written using FLASK (Python) to showcase backend coding.

## Flask Application Structure

```
.
├── README.md
├── app.log
├── config.py
├── flaskrun
├── main
│   ├── __init__.py
│   ├── crud
│   │   └── routes.py
│   ├── database.db
│   ├── features
│   │   └── routes.py
│   ├── forms.py
│   ├── models.py
│   ├── static
│   │   └── css
│   │       └── styles.css
│   ├── templates
│   │   └── index.html
│   └── views.py
├── requirements.txt
├── run.py
```

## Future Development
- New/different flask configurations can be added to config.py.
- New features can be added in main/features/routes.py.
- New page views can be added in main/views.py.
- New database tables can be created in main/models.py.
- More error handlers can be added in main/handlers.py.
  - A corresponding error page should be created in main/templates/errors/.

## Run using Replit

Using the `Shell` provided by Replit, run the following command to start the web application in production environment:
```
./flaskrun.sh 
```
Or run the following command to start the web application in development environment:
```
./flaskrun.sh development
```

Once the script finishes running, a browser should open, showcasing the web application. Click on the "Open in a new tab" icon to open the app in a bigger window (Recommended so that all elements load).


## Run on Windows environment
Please make sure that [Python](https://www.python.org/downloads/), pip, and git is installed.

Run the following command to clone the repository:
```
git clone https://github.com/giangm/shopify-challenge-fall-2022.git
```

Run the following command using `CMD` terminal to install required libraries and start the web application in production environment:
```
flaskrun.bat
```


## Run on Linux environment
Please make sure that [Python](https://www.python.org/downloads/), pip, and git is installed.

Run the following command to clone the repository:
```
git clone https://github.com/giangm/shopify-challenge-fall-2022.git
```

Run the following command using a terminal to install required libraries and start the web application in production environment:
```
flaskrun.sh
```


## Run with Docker
Please make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your system.

Run the following command to build the docker image:
```
docker build -t inventoryapp .
```
Run the following command to run the docker container:
```
docker run --rm --privileged -p 5000:5000 inventoryapp
```

Open `localhost:5000` in your browser to view web application.


## References

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/)
