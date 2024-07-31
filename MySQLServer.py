import mysql.connector
from mysql.connector import Error
def create_database():
    try:
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Kabe@9168Clde'
        )
        if mydb.is_connected():
          
          mycursor = mydb.cursor()
          try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            mydb.commit()
            print("Database 'alx_book_store' created successfully!")


          except Error as e:
            if "1007 (HY000): Can't create database" in str(e):
                print("Database 'alx_book_store' already exists!")
            else:
                print(f'error creating database {e}')
          finally:
        
            mycursor.close()
    except Error as e:
       print(f"Error connecting to MySQL: {e}")
    finally:
        if mydb.is_connected():
           mydb.close()
        print('Mysql connection is closed') 

