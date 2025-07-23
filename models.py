from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    mobile = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    amount = Column(Integer, primary_key=False)
    test = Column(String, primary_key=False)
    test1 = Column(Time, primary_key=False)
    saffds = Column(Time, primary_key=False)
    gdfgdf = Column(Time, primary_key=False)


class Records(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    username = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    pincode = Column(String, primary_key=False)
    user_amount = Column(Integer, primary_key=False)


class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    subject = Column(String, primary_key=False)


class Shivam(Base):
    __tablename__ = 'shivam'
    id = Column(Integer, primary_key=True)
    shivam = Column(Boolean, primary_key=False)


class Test123(Base):
    __tablename__ = 'test123'
    id = Column(Integer, primary_key=True)
    test123 = Column(String, primary_key=False)
    test1234 = Column(Integer, primary_key=False)


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    testqw23 = Column(String, primary_key=False)


class Keshav(Base):
    __tablename__ = 'keshav'
    id = Column(Integer, primary_key=True)
    test = Column(String, primary_key=False)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    test = Column(String, primary_key=False)
    test123 = Column(String, primary_key=False)


class Test45756765(Base):
    __tablename__ = 'test45756765'
    id = Column(Integer, primary_key=True)
    dsfdsfdgfd = Column(Integer, primary_key=False)
    scdfg = Column(Time, primary_key=False)


class Test1234(Base):
    __tablename__ = 'test1234'
    id = Column(Integer, primary_key=True)


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    age = Column(String, primary_key=False)


class Test123456789(Base):
    __tablename__ = 'test123456789'
    id = Column(Integer, primary_key=True)


class Trujghyr(Base):
    __tablename__ = 'trujghyr'
    id = Column(Integer, primary_key=True)
    fsg = Column(String, primary_key=False)


