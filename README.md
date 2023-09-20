This is an API built with Flask. It contains information on companion characters in the game Baldur's Gate 3.

# How to Run
1. Clone this repo: `git clone git@github.com:lanxeyu/flask_api.git`
2. In the project folder, create a **.flaskenv** (or **.env** if .flaskenv is not recognized) file and specify the following parameters within the file:<br>
    FLASK_APP=app<br>
    FLASK_DEBUG=1<br>
    DB_URL=*database URL of your choice*
3. Open a terminal in the project folder and enter: `pip install pipenv`
4. Install dependencies: `pipenv install`
5. Initialize database: `pipenv run seed` 
6. Start the API: `pipenv run dev`
7. Access the API on [localhost:5000](http://localhost:5000/)