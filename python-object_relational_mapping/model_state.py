"""We will import all the required modules"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


"""This is the super class"""

Base  = declarative_base()

"""This is a class representing the 'states' table"""
class State(Base):
    """This is the table declaration"""
    __tablename__ = "states"

    """These are the columns that will be in our state table"""
    id  = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    """Create an engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    """Create the states table"""
    Base.metadata.create_all(engine)