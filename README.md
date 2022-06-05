# wikipediaAPI
A RESTful API by Python and Flask to fetch 10 random articles from Wikipedia-api and store them in sqlite db. Then fetch them to the browser with details of each article e.g., title, first paragraph and an image.

## How It Works
- File db.py is responsible to:
  - fetch 10 random articles's titles from wikipedia-api
  - insert 10 random wikipedia titles into db
  - fetch and insert articles's data into db (title, summary, image)
- File app.py is responsible to:
  - fetch article's title and details using restapi to the browser
- File home.html preview the data to the user (html/js)

## Config
- pip install wikipedia-api
- pip install flask
- pip install virtualenv

## Database
- Sqlite3
- fetched data stored to the wiki-api.db file 

## Dependencies
- Python3 
- Sqlite3
- Requests
- Flask
- wikipedia-api
- virtualenv
- render_template
- html/js

## How to run
