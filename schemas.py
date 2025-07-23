from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Profile(BaseModel):
    name: Optional[str]=None
    address: Optional[str]=None
    mobile: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None
    amount: Optional[int]=None
    test: Optional[str]=None
    test1: Optional[datetime.time]=None
    saffds: Optional[datetime.time]=None
    gdfgdf: Optional[datetime.time]=None


class ReadProfile(BaseModel):
    name: Optional[str]=None
    address: Optional[str]=None
    mobile: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None
    amount: Optional[int]=None
    test: Optional[str]=None
    test1: Optional[datetime.time]=None
    saffds: Optional[datetime.time]=None
    gdfgdf: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Records(BaseModel):
    username: Optional[str]=None
    address: Optional[str]=None
    pincode: Optional[str]=None
    user_amount: Optional[int]=None


class ReadRecords(BaseModel):
    username: Optional[str]=None
    address: Optional[str]=None
    pincode: Optional[str]=None
    user_amount: Optional[int]=None
    class Config:
        from_attributes = True


class Class(BaseModel):
    subject: Optional[str]=None


class ReadClass(BaseModel):
    subject: Optional[str]=None
    class Config:
        from_attributes = True


class Shivam(BaseModel):
    shivam: Optional[bool]=None


class ReadShivam(BaseModel):
    shivam: Optional[bool]=None
    class Config:
        from_attributes = True


class Test123(BaseModel):
    test123: Optional[str]=None
    test1234: Optional[int]=None


class ReadTest123(BaseModel):
    test123: Optional[str]=None
    test1234: Optional[int]=None
    class Config:
        from_attributes = True


class Test(BaseModel):
    testqw23: Optional[str]=None


class ReadTest(BaseModel):
    testqw23: Optional[str]=None
    class Config:
        from_attributes = True


class Keshav(BaseModel):
    test: Optional[str]=None


class ReadKeshav(BaseModel):
    test: Optional[str]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    username: Optional[str]=None
    password: Optional[str]=None
    test: Optional[str]=None
    test123: Optional[str]=None


class ReadUsers(BaseModel):
    username: Optional[str]=None
    password: Optional[str]=None
    test: Optional[str]=None
    test123: Optional[str]=None
    class Config:
        from_attributes = True


class Test45756765(BaseModel):
    scdfg: Optional[datetime.time]=None


class ReadTest45756765(BaseModel):
    scdfg: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Test1234(BaseModel):
    pass


class ReadTest1234(BaseModel):
    class Config:
        from_attributes = True


class Students(BaseModel):
    name: Optional[str]=None
    age: Optional[str]=None


class ReadStudents(BaseModel):
    name: Optional[str]=None
    age: Optional[str]=None
    class Config:
        from_attributes = True


class Test123456789(BaseModel):
    pass


class ReadTest123456789(BaseModel):
    class Config:
        from_attributes = True


class Trujghyr(BaseModel):
    fsg: Optional[str]=None


class ReadTrujghyr(BaseModel):
    fsg: Optional[str]=None
    class Config:
        from_attributes = True




class PostClass(BaseModel):
    id: Optional[int]=None
    subject: Optional[str]=None

    class Config:
        from_attributes = True



class PutClassId(BaseModel):
    id: Optional[int]=None
    subject: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteClassId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostShivam(BaseModel):
    id: Optional[int]=None
    shivam: Optional[bool]=None

    class Config:
        from_attributes = True



class PutShivamId(BaseModel):
    id: Optional[int]=None
    shivam: Optional[bool]=None

    class Config:
        from_attributes = True



class DeleteShivamId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest123(BaseModel):
    id: Optional[int]=None
    test123: Optional[str]=None
    test1234: Optional[int]=None

    class Config:
        from_attributes = True



class PutTest123Id(BaseModel):
    id: Optional[int]=None
    test123: Optional[str]=None
    test1234: Optional[int]=None

    class Config:
        from_attributes = True



class DeleteTest123Id(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest(BaseModel):
    id: Optional[int]=None
    testqw23: Optional[str]=None

    class Config:
        from_attributes = True



class PutTestId(BaseModel):
    id: Optional[int]=None
    testqw23: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteTestId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostKeshav(BaseModel):
    id: Optional[int]=None
    test: Optional[str]=None

    class Config:
        from_attributes = True



class PutKeshavId(BaseModel):
    id: Optional[int]=None
    test: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteKeshavId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTrujghyr(BaseModel):
    id: Optional[int]=None
    fsg: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteTest123456789Id(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    password: Optional[str]=None
    test: Optional[str]=None
    test123: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    password: Optional[str]=None
    test: Optional[str]=None
    test123: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteUsersId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest45756765(BaseModel):
    id: Optional[int]=None
    dsfdsfdgfd: Optional[int]=None
    scdfg: Optional[Any]=None

    class Config:
        from_attributes = True



class PutTest45756765Id(BaseModel):
    id: Optional[int]=None
    dsfdsfdgfd: Optional[int]=None
    scdfg: Optional[Any]=None

    class Config:
        from_attributes = True



class DeleteTest45756765Id(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest1234(BaseModel):
    id: Optional[int]=None

    class Config:
        from_attributes = True



class PutTest1234Id(BaseModel):
    id: Optional[int]=None

    class Config:
        from_attributes = True



class DeleteTest1234Id(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    age: Optional[str]=None

    class Config:
        from_attributes = True



class PostProfile(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    address: Optional[str]=None
    mobile: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None
    amount: Optional[int]=None
    test: Optional[str]=None
    test1: Optional[Any]=None
    saffds: Optional[Any]=None
    gdfgdf: Optional[Any]=None

    class Config:
        from_attributes = True



class PutProfileId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    address: Optional[str]=None
    mobile: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None
    amount: Optional[int]=None
    test: Optional[str]=None
    test1: Optional[Any]=None
    saffds: Optional[Any]=None
    gdfgdf: Optional[Any]=None

    class Config:
        from_attributes = True



class DeleteProfileId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostRecords(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    address: Optional[str]=None
    pincode: Optional[str]=None
    user_amount: Optional[int]=None

    class Config:
        from_attributes = True



class PutRecordsId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    address: Optional[str]=None
    pincode: Optional[str]=None
    user_amount: Optional[int]=None

    class Config:
        from_attributes = True



class DeleteRecordsId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PutStudentsId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    age: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteStudentsId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest123456789(BaseModel):
    id: Optional[int]=None

    class Config:
        from_attributes = True



class PutTest123456789Id(BaseModel):
    id: Optional[int]=None

    class Config:
        from_attributes = True



class PutTrujghyrId(BaseModel):
    id: Optional[int]=None
    fsg: Optional[str]=None

    class Config:
        from_attributes = True



class DeleteTrujghyrId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True

