
from github import Github
import os
from pprint import pprint
import requests
import sqlite3
from sqlite3 import Error
 
con = sqlite3.connect('example.db')

class Seed:

    def get_git_users(self, total):
        g = Github("975025cbb60248fb3cec01bb6042d6acee309fa4")
        arr_git_users = []
        
        iterator = 0
        for u in g.get_users():
            if iterator < total:              

                username  = u.login            
                user_data = g.get_user(username)            
                git_users = (user_data.id, u.login, user_data.avatar_url, user_data.type, user_data.html_url)
                         
                arr_git_users.append(git_users)
                iterator+=1
            else:
                break

        return arr_git_users

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_item(conn, item):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id

    """
    sql = " INSERT INTO users(id,login,avatar_url, type, profile_url) VALUES(?,?,?,?,?) "
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"test.db"

    git_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        login text NOT NULL,
                                        avatar_url text,
                                        type text,
                                        profile_url text
                                    ); """

    # create a database connection
    conn = create_connection(database)
 


if __name__ == '__main__':
    main()