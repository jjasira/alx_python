"""We will import all the required modules"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

"""To prevent the script from executing when importing"""
if __name__ == '__main__':
    """We assign the command line arguments"""
    username, password, database = sys.argv[1:]

    """create an engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    """create a session to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        """Write a query with sqlalchemy to fetch all the Objects and Order by id"""
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all

        """Display the results"""
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    except Exception as e:
        print("Error:", e)
    finally:
        """Close the session"""
        session.close()