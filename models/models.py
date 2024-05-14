from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MslData(Base):
    __tablename__ = 'msl_data'
    id = Column(Integer, primary_key=True, unique=True)
    thickness_level = Column(String)
    moisture_level = Column(String)
    hours_greater_than_72 = Column(Float)
    hours_less_than_72 = Column(Float)


class CarrierData(Base):
    __tablename__ = 'carrier_data'
    id = Column(Integer, primary_key=True, unique=True)
    carrier_id = Column(String, unique=True)
    part_name = Column(String)


class TaskData(Base):
    __tablename__ = 'task_data'
    id = Column(Integer, primary_key=True, unique=True)
    carrier_id = Column(Integer, unique=True)
    part_name = Column(String)
    thickness = Column(String)
    msl = Column(String)
    time_after_before_72_hours = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    set_time = Column(String)
    total_time = Column(String)
    carrier_position = Column(String)

# Create table for storing part msl history to remember last msl set



# Set up the engine to connect to the SQLite database
engine = create_engine('sqlite:///../database.db', echo=True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()
