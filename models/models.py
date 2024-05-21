from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, Interval
from database import Base
# from sqlalchemy.orm import sessionmaker
#


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
    carrier_id = Column(Integer)
    part_name = Column(String)
    thickness = Column(String)
    msl = Column(String)
    time_after_before_72_hours = Column(String)
    drying_start_interval = Column(Interval)
    add_interval = Column(Interval)
    total_time = Column(Interval)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    carrier_position = Column(String)
    in_dryer = Column(Boolean)
    drying_finished = Column(Boolean)


# engine = create_engine('sqlite:///../database.db')
# Base.metadata.create_all(engine)
#
# # Create a session
# Session = sessionmaker(bind=engine)