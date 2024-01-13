"""We wimport all the needed modules"""
import MySQLdb
"""The sys module will enable us to get the command line arguments"""
import sys

"""This prevents the code from running automatically when imported"""
if __name__ == '__main__':
    """We assign the command line arguments to varibales"""
    mysql_username, mysql_password, database_name = sys.argv[1:4]

    """We establish a connection to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd= mysql_password, db=database_name)

    """We create a cursor object that will enable us write the sql queries directly into out python script"""
    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    """We execute the required query"""
   
    cursor.execute(query)

    """Fetch all the rows"""
    rows = cursor.fetchall()

    """Display the result by looping over the rows"""
    for row in rows:
        print(row)

    """Close the connection"""
    cursor.close()
    db.close()