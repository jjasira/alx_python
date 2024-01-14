"""We wimport all the needed modules"""
import MySQLdb
"""The sys module will enable us to get the command line arguments"""
import sys

"""This prevents the code from running automatically when imported"""
if __name__ == '__main__':
    """We assign the command line arguments to varibales"""
    mysql_username, mysql_password, database_name, state_name = sys.argv[1:]

    """We establish a connection to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd= mysql_password, db=database_name)

    """We create a cursor object that will enable us write the sql queries directly into out python script"""
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    """We execute the required query"""
    try:
        cursor.execute(query, (state_name,))

        """Fetch all the results"""
        cities = cursor.fetchall()

        """Display the results"""
        if cities:
            print(", ".join(city[0] for city in cities))
        else:
            print("")
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    
    finally:

        """Close the connection"""
        cursor.close()
        db.close()