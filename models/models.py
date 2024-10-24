from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base

declarative_base()

class MslData(declarative_base()):
    __tablename__ = 'msl_data'
    id = Column(Integer, primary_key=True, unique=True)
    thickness_level = Column(String)
    moisture_level = Column(String)
    hours_greater_than_72 = Column(Float)
    hours_less_than_72 = Column(Float)


class CarrierData(declarative_base()):
    __tablename__ = 'carrier_data'
    id = Column(Integer, primary_key=True, unique=True)
    carrier_id = Column(String, unique=True)
    part_name = Column(String)


class TaskData(declarative_base()):
    __tablename__ = 'task_data'
    id = Column(Integer, primary_key=True, unique=True)
    carrier_id = Column(String)
    part_name = Column(String)
    thickness = Column(String)
    msl = Column(String)
    hours_less_72_hours = Column(Boolean, default=False)
    hours_greater_than_72 = Column(Boolean, default=False)
    drying_start_interval = Column(String)
    add_interval = Column(String)
    total_time = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    carrier_position = Column(String)
    in_dryer = Column(Boolean)
    drying_finished = Column(Boolean)


class ActivityRegister(declarative_base()):
    __tablename__ = 'activity_register'
    id = Column(Integer, primary_key=True, unique=True)
    time = Column(DateTime)
