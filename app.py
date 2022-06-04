from crypt import methods
from flask import Flask,render_template,request
from db import fetchTitlesTableData
from db import fetchPagesTableData


import sqlite3 as sql 

app = Flask(__name__)

@app.route('/titles', methods=['GET'])
def viewTitles():
    return render_template("home.html", artTitles = fetchTitlesTableData(), pagesDetails = fetchPagesTableData())

# @app.route('/pages', methods=['GET'])
# def viewPagesById():
#     return render_template("pages.html", pagesDetails = fetchPagesTableData())



if __name__ == '__main__':
    app.run(debug=True)
