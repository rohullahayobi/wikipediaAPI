
import wikipedia
import sqlite3
import requests


###################FETCHING DATA####################

#fetch all titles from TITLES table
def fetchTitlesTableData():
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        sqlite_select_query = """SELECT rowid, title from titles"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Printing each row")
        for row in records:
            print(row)
        #     print(row[1])
        #     print("\n")
        # print(records[0])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from TILES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return records
# fetchTitlesTableData()


#fetch all pages details from PAGES table
def fetchPagesTableData():
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from pages"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # print("Printing each row")
        for row in records:
            row

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from PAGES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return records                     
# fetchPagesTableData()



#############DELETING DATA ######################

#delete Titles table data
def deleteTitlesData():
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #delete pages table data
        sqlite_create_table_query = '''DELETE FROM Titles;'''

        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite TITLES table deleted")


    except sqlite3.Error as error:
        print("Failed to delete data from TITLES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

deleteTitlesData()

#delete PAGES table data
def deleteTableData():
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #delete pages table data
        sqlite_create_table_query = '''DELETE FROM pages;'''

        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite PAGES table deleted")


    except sqlite3.Error as error:
        print("Failed to delete data from PAGES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

deleteTableData()


#fetch random articles's titles from WIKIPEDIA API
ranData = wikipedia.random(pages=10)



#############CREATE TABLES AND INSERT DATA ############################

#insert 10 random wikipedia titles into the TITLES table
def insertIntoTitlesTable(title):
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #create table
        sqlite_create_table_query = "CREATE TABLE IF NOT EXISTS titles (title TEXT NOT NULL);"

        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite TITLES table created successfully")

        #insert data
        for item in title:
            cursor.execute("INSERT INTO titles VALUES (?);", (item,))
        sqliteConnection.commit()
        print("10 Random Titles from WIKIPEDIA API inserted successfully into TITLES table")
        cursor.close()


    except sqlite3.Error as error:
        print("Failed to insert random titles into sqlite TITLES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertIntoTitlesTable(ranData)



#create and insert data into PAGES table
def insertWikiPediaDataIntoPagesTable(id, title, summary, image):
    try:
        sqliteConnection = sqlite3.connect('wiki_api.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #create table PAGES
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS pages (
                                id INTEGER PRIMARY KEY,
                                title TEXT NOT NULL,
                                summary TEXT NOT NULL,
                                image BLOB);'''

        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite PAGES table created successfully")

        #insert data
        sqlite_insert_with_param = """INSERT INTO pages
                          (id, title, summary, image) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (id, title, summary, image)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Detials of titles successfully inserted into PAGES table")
        cursor.close()


    except sqlite3.Error as error:
        print("Failed to insert titles details into PAGES table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

#get the random titles from the TITLES table in database 
artIdTitles = fetchTitlesTableData()
id1 = artIdTitles[0][0]
t1 = artIdTitles[0][1]

id2 = artIdTitles[1][0]
t2 = artIdTitles[1][1]

id3 = artIdTitles[2][0]
t3 = artIdTitles[2][1]

id4 = artIdTitles[3][0]
t4 = artIdTitles[3][1]

id5 = artIdTitles[4][0]
t5 = artIdTitles[4][1]

id6 = artIdTitles[5][0]
t6 = artIdTitles[5][1]

id7 = artIdTitles[6][0]
t7 = artIdTitles[6][1]

id8 = artIdTitles[7][0]
t8 = artIdTitles[7][1]

id9 = artIdTitles[8][0]
t9 = artIdTitles[8][1]

id10 = artIdTitles[9][0]
t10 = artIdTitles[9][1]

# fetch details of titles from wikipedia api
#Title 1
t = wikipedia.page(t1)
title1 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t1)
sumjson = sumuri.json()
summary1 = sumjson["extract"]
image1 = t.images[0]

#Title 2
t = wikipedia.page(t2)
title2 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t2)
sumjson = sumuri.json()
summary2 = sumjson["extract"]
image2 = t.images[0]

#Title 3
t = wikipedia.page(t3)
title3 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t3)
sumjson = sumuri.json()
summary3 = sumjson["extract"]
image3 = t.images[0]

#Title 4
t = wikipedia.page(t4)
title4 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t4)
sumjson = sumuri.json()
summary4 = sumjson["extract"]
image4 = t.images[0]

#Title 5
t = wikipedia.page(t5)
title5 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t5)
sumjson = sumuri.json()
summary5 = sumjson["extract"]
image5 = t.images[0]

#Title 6
t = wikipedia.page(t6)
title6 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t6)
sumjson = sumuri.json()
summary6 = sumjson["extract"]
image6 = t.images[0]

#Title 7
t = wikipedia.page(t7)
title7 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t7)
sumjson = sumuri.json()
summary7 = sumjson["extract"]
image7 = t.images[0]

#Title 8
t = wikipedia.page(t8)
title8 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t8)
sumjson = sumuri.json()
summary8 = sumjson["extract"]
image8 = t.images[0]

#Title 9
t = wikipedia.page(t9)
title9 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t9)
sumjson = sumuri.json()
summary9 = sumjson["extract"]
image9 = t.images[0]

# Title 10
t = wikipedia.page(t10)
title10 = t.title
sumuri = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/%s" % t10)
sumjson = sumuri.json()
summary10 = sumjson["extract"]
image10 = t.images[0]

# insert details into database
insertWikiPediaDataIntoPagesTable(id1, title1, summary1, image1)
insertWikiPediaDataIntoPagesTable(id2, title2, summary2, image2)
insertWikiPediaDataIntoPagesTable(id3, title3, summary3, image3)
insertWikiPediaDataIntoPagesTable(id4, title4, summary4, image4)
insertWikiPediaDataIntoPagesTable(id5, title5, summary5, image5)
insertWikiPediaDataIntoPagesTable(id6, title6, summary6, image6)
insertWikiPediaDataIntoPagesTable(id7, title7, summary7, image7)
insertWikiPediaDataIntoPagesTable(id8, title8, summary8, image8)
insertWikiPediaDataIntoPagesTable(id9, title9, summary9, image9)
insertWikiPediaDataIntoPagesTable(id10, title10, summary10, image10)







