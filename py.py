# ------------------------------------------------
#  create datebase programming => using sqlite3
# ------------------------------------------------

# import library

import sqlite3

import requests


# start def for collect all commends

def collect_all():

    '''
        funcation for create database"app.db"
        ,create table user ,you  can add the user 
        id and name form user_to_insert and its add
        to the datebase
    '''

    try:

        # start connect for datebace

        db = sqlite3.connect("app.db")


        # start cursor

        cr = db.cursor()

        # create tables and rows

        cr.execute("CREATE TABLE IF NOT EXISTS user(id integer, name text)")
        # Define the rows to be inserted
        user_to_insert = [
            (1, 'yossef'),
            (2, 'farouk'),
            (3, 'ahmed')
            ]

        # Loop over the rows and insert them if they don't already exist
        for row in user_to_insert:
            cr.execute("SELECT id FROM user WHERE id = ?", (row[0],))
            existing_row = cr.fetchone()
            if existing_row is None:
                cr.execute("INSERT INTO user(id, name) VALUES (?, ?)", row)
        # fetch data

        cr.execute("select * from user")

        # start fetch

        resutls = cr.fetchall()


        # message connect success

        print("- connect successful to database -")

        # Save (Commit) Changes

        db.commit()

    except:

        print("- error happend -")


    else:

        print(f"- the user in is database is {len(resutls)} -")

        for row in resutls:

            print(f"- UserID => {row[0]}, -", end=" ")

            print(f"- Username => {row[1]} -")

    finally:
        if (db):

            # Close Database Connection
            db.close()

            print("- database is closed -\n")



# start funcation
collect_all()


# print(help(collect_all))

# connect me

url = "https://github.com/yossefsabry"

output = f"<a href='{url}'></a> "

response = requests.get(url)
print('--- connect me  ---')
print(output)
print('-------------------')