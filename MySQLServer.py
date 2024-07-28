import mysql.connector
from mysql.connector import errorcode

def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{db_name}' already exists.")
        else:
            print(f"Failed creating database: {err}")

def main():
    # Define your MySQL connection parameters
    config = {
        'user': 'root',
        'password': 'Kabe@9168Clde',
        'host': 'localhost'
    }

    try:
        # Establish a connection to MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Database name
        db_name = 'alx_book_store'

        # Create the database
        create_database(cursor, db_name)

        # Close the cursor and connection
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    else:
        print("Connection to MySQL server closed.")

if __name__ == '__main__':
    main()


