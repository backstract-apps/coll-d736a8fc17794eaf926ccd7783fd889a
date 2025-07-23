from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_class(db: Session):

    query = db.query(models.Class)

    class_all = query.all()
    class_all = (
        [new_data.to_dict() for new_data in class_all] if class_all else class_all
    )
    res = {
        "class_all": class_all,
    }
    return res


async def get_class_id(db: Session, id: int):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    class_one = query.first()

    class_one = (
        (class_one.to_dict() if hasattr(class_one, "to_dict") else vars(class_one))
        if class_one
        else class_one
    )

    res = {
        "class_one": class_one,
    }
    return res


async def post_class(db: Session, raw_data: schemas.PostClass):
    id: int = raw_data.id
    subject: str = raw_data.subject

    record_to_be_added = {"id": id, "subject": subject}
    new_class = models.Class(**record_to_be_added)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    class_inserted_record = new_class.to_dict()

    res = {
        "class_inserted_record": class_inserted_record,
    }
    return res


async def get_trujghyr_id(db: Session, id: int):

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))

    trujghyr_one = query.first()

    trujghyr_one = (
        (
            trujghyr_one.to_dict()
            if hasattr(trujghyr_one, "to_dict")
            else vars(trujghyr_one)
        )
        if trujghyr_one
        else trujghyr_one
    )

    res = {
        "trujghyr_one": trujghyr_one,
    }
    return res


async def put_class_id(db: Session, raw_data: schemas.PutClassId):
    id: int = raw_data.id
    subject: str = raw_data.subject

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))
    class_edited_record = query.first()

    if class_edited_record:
        for key, value in {"id": id, "subject": subject}.items():
            setattr(class_edited_record, key, value)

        db.commit()
        db.refresh(class_edited_record)

        class_edited_record = (
            class_edited_record.to_dict()
            if hasattr(class_edited_record, "to_dict")
            else vars(class_edited_record)
        )
    res = {
        "class_edited_record": class_edited_record,
    }
    return res


async def delete_class_id(db: Session, raw_data: schemas.DeleteClassId):
    id: int = raw_data.id

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        class_deleted = record_to_delete.to_dict()
    else:
        class_deleted = record_to_delete
    res = {
        "class_deleted": class_deleted,
    }
    return res


async def get_shivam(db: Session):

    query = db.query(models.Shivam)

    shivam_all = query.all()
    shivam_all = (
        [new_data.to_dict() for new_data in shivam_all] if shivam_all else shivam_all
    )
    res = {
        "shivam_all": shivam_all,
    }
    return res


async def get_shivam_id(db: Session, id: int):

    query = db.query(models.Shivam)
    query = query.filter(and_(models.Shivam.id == id))

    shivam_one = query.first()

    shivam_one = (
        (shivam_one.to_dict() if hasattr(shivam_one, "to_dict") else vars(shivam_one))
        if shivam_one
        else shivam_one
    )

    res = {
        "shivam_one": shivam_one,
    }
    return res


async def post_shivam(db: Session, raw_data: schemas.PostShivam):
    id: int = raw_data.id
    shivam: bool = raw_data.shivam

    record_to_be_added = {"id": id, "shivam": shivam}
    new_shivam = models.Shivam(**record_to_be_added)
    db.add(new_shivam)
    db.commit()
    db.refresh(new_shivam)
    shivam_inserted_record = new_shivam.to_dict()

    res = {
        "shivam_inserted_record": shivam_inserted_record,
    }
    return res


async def put_shivam_id(db: Session, raw_data: schemas.PutShivamId):
    id: int = raw_data.id
    shivam: bool = raw_data.shivam

    query = db.query(models.Shivam)
    query = query.filter(and_(models.Shivam.id == id))
    shivam_edited_record = query.first()

    if shivam_edited_record:
        for key, value in {"id": id, "shivam": shivam}.items():
            setattr(shivam_edited_record, key, value)

        db.commit()
        db.refresh(shivam_edited_record)

        shivam_edited_record = (
            shivam_edited_record.to_dict()
            if hasattr(shivam_edited_record, "to_dict")
            else vars(shivam_edited_record)
        )
    res = {
        "shivam_edited_record": shivam_edited_record,
    }
    return res


async def delete_shivam_id(db: Session, raw_data: schemas.DeleteShivamId):
    id: int = raw_data.id

    query = db.query(models.Shivam)
    query = query.filter(and_(models.Shivam.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        shivam_deleted = record_to_delete.to_dict()
    else:
        shivam_deleted = record_to_delete
    res = {
        "shivam_deleted": shivam_deleted,
    }
    return res


async def get_test123(db: Session):

    query = db.query(models.Test123)

    test123_all = query.all()
    test123_all = (
        [new_data.to_dict() for new_data in test123_all] if test123_all else test123_all
    )
    res = {
        "test123_all": test123_all,
    }
    return res


async def get_test123_id(db: Session, id: int):

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))

    test123_one = query.first()

    test123_one = (
        (
            test123_one.to_dict()
            if hasattr(test123_one, "to_dict")
            else vars(test123_one)
        )
        if test123_one
        else test123_one
    )

    res = {
        "test123_one": test123_one,
    }
    return res


async def post_test123(db: Session, raw_data: schemas.PostTest123):
    id: int = raw_data.id
    test123: str = raw_data.test123
    test1234: int = raw_data.test1234

    record_to_be_added = {"id": id, "test123": test123, "test1234": test1234}
    new_test123 = models.Test123(**record_to_be_added)
    db.add(new_test123)
    db.commit()
    db.refresh(new_test123)
    test123_inserted_record = new_test123.to_dict()

    res = {
        "test123_inserted_record": test123_inserted_record,
    }
    return res


async def put_test123_id(db: Session, raw_data: schemas.PutTest123Id):
    id: int = raw_data.id
    test123: str = raw_data.test123
    test1234: int = raw_data.test1234

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))
    test123_edited_record = query.first()

    if test123_edited_record:
        for key, value in {"id": id, "test123": test123, "test1234": test1234}.items():
            setattr(test123_edited_record, key, value)

        db.commit()
        db.refresh(test123_edited_record)

        test123_edited_record = (
            test123_edited_record.to_dict()
            if hasattr(test123_edited_record, "to_dict")
            else vars(test123_edited_record)
        )
    res = {
        "test123_edited_record": test123_edited_record,
    }
    return res


async def delete_test123_id(db: Session, raw_data: schemas.DeleteTest123Id):
    id: int = raw_data.id

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test123_deleted = record_to_delete.to_dict()
    else:
        test123_deleted = record_to_delete
    res = {
        "test123_deleted": test123_deleted,
    }
    return res


async def get_test(db: Session):

    query = db.query(models.Test)

    test_all = query.all()
    test_all = [new_data.to_dict() for new_data in test_all] if test_all else test_all
    res = {
        "test_all": test_all,
    }
    return res


async def get_test_id(db: Session, id: int):

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    test_one = query.first()

    test_one = (
        (test_one.to_dict() if hasattr(test_one, "to_dict") else vars(test_one))
        if test_one
        else test_one
    )

    res = {
        "test_one": test_one,
    }
    return res


async def post_test(db: Session, raw_data: schemas.PostTest):
    id: int = raw_data.id
    testqw23: str = raw_data.testqw23

    record_to_be_added = {"id": id, "testqw23": testqw23}
    new_test = models.Test(**record_to_be_added)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    test_inserted_record = new_test.to_dict()

    res = {
        "test_inserted_record": test_inserted_record,
    }
    return res


async def put_test_id(db: Session, raw_data: schemas.PutTestId):
    id: int = raw_data.id
    testqw23: str = raw_data.testqw23

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))
    test_edited_record = query.first()

    if test_edited_record:
        for key, value in {"id": id, "testqw23": testqw23}.items():
            setattr(test_edited_record, key, value)

        db.commit()
        db.refresh(test_edited_record)

        test_edited_record = (
            test_edited_record.to_dict()
            if hasattr(test_edited_record, "to_dict")
            else vars(test_edited_record)
        )
    res = {
        "test_edited_record": test_edited_record,
    }
    return res


async def delete_test_id(db: Session, raw_data: schemas.DeleteTestId):
    id: int = raw_data.id

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test_deleted = record_to_delete.to_dict()
    else:
        test_deleted = record_to_delete
    res = {
        "test_deleted": test_deleted,
    }
    return res


async def get_keshav(db: Session):

    query = db.query(models.Keshav)

    keshav_all = query.all()
    keshav_all = (
        [new_data.to_dict() for new_data in keshav_all] if keshav_all else keshav_all
    )
    res = {
        "keshav_all": keshav_all,
    }
    return res


async def get_keshav_id(db: Session, id: int):

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))

    keshav_one = query.first()

    keshav_one = (
        (keshav_one.to_dict() if hasattr(keshav_one, "to_dict") else vars(keshav_one))
        if keshav_one
        else keshav_one
    )

    res = {
        "keshav_one": keshav_one,
    }
    return res


async def post_keshav(db: Session, raw_data: schemas.PostKeshav):
    id: int = raw_data.id
    test: str = raw_data.test

    record_to_be_added = {"id": id, "test": test}
    new_keshav = models.Keshav(**record_to_be_added)
    db.add(new_keshav)
    db.commit()
    db.refresh(new_keshav)
    keshav_inserted_record = new_keshav.to_dict()

    res = {
        "keshav_inserted_record": keshav_inserted_record,
    }
    return res


async def put_keshav_id(db: Session, raw_data: schemas.PutKeshavId):
    id: int = raw_data.id
    test: str = raw_data.test

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))
    keshav_edited_record = query.first()

    if keshav_edited_record:
        for key, value in {"id": id, "test": test}.items():
            setattr(keshav_edited_record, key, value)

        db.commit()
        db.refresh(keshav_edited_record)

        keshav_edited_record = (
            keshav_edited_record.to_dict()
            if hasattr(keshav_edited_record, "to_dict")
            else vars(keshav_edited_record)
        )
    res = {
        "keshav_edited_record": keshav_edited_record,
    }
    return res


async def delete_keshav_id(db: Session, raw_data: schemas.DeleteKeshavId):
    id: int = raw_data.id

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        keshav_deleted = record_to_delete.to_dict()
    else:
        keshav_deleted = record_to_delete
    res = {
        "keshav_deleted": keshav_deleted,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_trujghyr(db: Session, raw_data: schemas.PostTrujghyr):
    id: int = raw_data.id
    fsg: str = raw_data.fsg

    record_to_be_added = {"id": id, "fsg": fsg}
    new_trujghyr = models.Trujghyr(**record_to_be_added)
    db.add(new_trujghyr)
    db.commit()
    db.refresh(new_trujghyr)
    trujghyr_inserted_record = new_trujghyr.to_dict()

    res = {
        "trujghyr_inserted_record": trujghyr_inserted_record,
    }
    return res


async def delete_test123456789_id(db: Session, raw_data: schemas.DeleteTest123456789Id):
    id: int = raw_data.id

    query = db.query(models.Test123456789)
    query = query.filter(and_(models.Test123456789.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test123456789_deleted = record_to_delete.to_dict()
    else:
        test123456789_deleted = record_to_delete
    res = {
        "test123456789_deleted": test123456789_deleted,
    }
    return res


async def get_trujghyr(db: Session):

    query = db.query(models.Trujghyr)

    trujghyr_all = query.all()
    trujghyr_all = (
        [new_data.to_dict() for new_data in trujghyr_all]
        if trujghyr_all
        else trujghyr_all
    )
    res = {
        "trujghyr_all": trujghyr_all,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    username: str = raw_data.username
    password: str = raw_data.password
    test: str = raw_data.test
    test123: str = raw_data.test123

    record_to_be_added = {
        "id": id,
        "test": test,
        "test123": test123,
        "password": password,
        "username": username,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    username: str = raw_data.username
    password: str = raw_data.password
    test: str = raw_data.test
    test123: str = raw_data.test123

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "test": test,
            "test123": test123,
            "password": password,
            "username": username,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, raw_data: schemas.DeleteUsersId):
    id: int = raw_data.id

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_test45756765(db: Session):

    query = db.query(models.Test45756765)

    test45756765_all = query.all()
    test45756765_all = (
        [new_data.to_dict() for new_data in test45756765_all]
        if test45756765_all
        else test45756765_all
    )
    res = {
        "test45756765_all": test45756765_all,
    }
    return res


async def get_test45756765_id(db: Session, id: int):

    query = db.query(models.Test45756765)
    query = query.filter(and_(models.Test45756765.id == id))

    test45756765_one = query.first()

    test45756765_one = (
        (
            test45756765_one.to_dict()
            if hasattr(test45756765_one, "to_dict")
            else vars(test45756765_one)
        )
        if test45756765_one
        else test45756765_one
    )

    res = {
        "test45756765_one": test45756765_one,
    }
    return res


async def post_test45756765(db: Session, raw_data: schemas.PostTest45756765):
    id: int = raw_data.id
    dsfdsfdgfd: int = raw_data.dsfdsfdgfd
    scdfg: datetime.datetime = raw_data.scdfg

    record_to_be_added = {"id": id, "scdfg": scdfg, "dsfdsfdgfd": dsfdsfdgfd}
    new_test45756765 = models.Test45756765(**record_to_be_added)
    db.add(new_test45756765)
    db.commit()
    db.refresh(new_test45756765)
    test45756765_inserted_record = new_test45756765.to_dict()

    res = {
        "test45756765_inserted_record": test45756765_inserted_record,
    }
    return res


async def put_test45756765_id(db: Session, raw_data: schemas.PutTest45756765Id):
    id: int = raw_data.id
    dsfdsfdgfd: int = raw_data.dsfdsfdgfd
    scdfg: datetime.datetime = raw_data.scdfg

    query = db.query(models.Test45756765)
    query = query.filter(and_(models.Test45756765.id == id))
    test45756765_edited_record = query.first()

    if test45756765_edited_record:
        for key, value in {"id": id, "scdfg": scdfg, "dsfdsfdgfd": dsfdsfdgfd}.items():
            setattr(test45756765_edited_record, key, value)

        db.commit()
        db.refresh(test45756765_edited_record)

        test45756765_edited_record = (
            test45756765_edited_record.to_dict()
            if hasattr(test45756765_edited_record, "to_dict")
            else vars(test45756765_edited_record)
        )
    res = {
        "test45756765_edited_record": test45756765_edited_record,
    }
    return res


async def delete_test45756765_id(db: Session, raw_data: schemas.DeleteTest45756765Id):
    id: int = raw_data.id

    query = db.query(models.Test45756765)
    query = query.filter(and_(models.Test45756765.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test45756765_deleted = record_to_delete.to_dict()
    else:
        test45756765_deleted = record_to_delete
    res = {
        "test45756765_deleted": test45756765_deleted,
    }
    return res


async def get_test1234(db: Session):

    query = db.query(models.Test1234)

    test1234_all = query.all()
    test1234_all = (
        [new_data.to_dict() for new_data in test1234_all]
        if test1234_all
        else test1234_all
    )
    res = {
        "test1234_all": test1234_all,
    }
    return res


async def get_test1234_id(db: Session, id: int):

    query = db.query(models.Test1234)
    query = query.filter(and_(models.Test1234.id == id))

    test1234_one = query.first()

    test1234_one = (
        (
            test1234_one.to_dict()
            if hasattr(test1234_one, "to_dict")
            else vars(test1234_one)
        )
        if test1234_one
        else test1234_one
    )

    res = {
        "test1234_one": test1234_one,
    }
    return res


async def post_test1234(db: Session, raw_data: schemas.PostTest1234):
    id: int = raw_data.id

    record_to_be_added = {"id": id}
    new_test1234 = models.Test1234(**record_to_be_added)
    db.add(new_test1234)
    db.commit()
    db.refresh(new_test1234)
    test1234_inserted_record = new_test1234.to_dict()

    res = {
        "test1234_inserted_record": test1234_inserted_record,
    }
    return res


async def put_test1234_id(db: Session, raw_data: schemas.PutTest1234Id):
    id: int = raw_data.id

    query = db.query(models.Test1234)
    query = query.filter(and_(models.Test1234.id == id))
    test1234_edited_record = query.first()

    if test1234_edited_record:
        for key, value in {"id": id}.items():
            setattr(test1234_edited_record, key, value)

        db.commit()
        db.refresh(test1234_edited_record)

        test1234_edited_record = (
            test1234_edited_record.to_dict()
            if hasattr(test1234_edited_record, "to_dict")
            else vars(test1234_edited_record)
        )
    res = {
        "test1234_edited_record": test1234_edited_record,
    }
    return res


async def delete_test1234_id(db: Session, raw_data: schemas.DeleteTest1234Id):
    id: int = raw_data.id

    query = db.query(models.Test1234)
    query = query.filter(and_(models.Test1234.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test1234_deleted = record_to_delete.to_dict()
    else:
        test1234_deleted = record_to_delete
    res = {
        "test1234_deleted": test1234_deleted,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    id: int = raw_data.id
    name: str = raw_data.name
    age: str = raw_data.age

    record_to_be_added = {"id": id, "age": age, "name": name}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def get_profile(db: Session):

    query = db.query(models.Profile)

    profile_all = query.all()
    profile_all = (
        [new_data.to_dict() for new_data in profile_all] if profile_all else profile_all
    )
    res = {
        "profile_all": profile_all,
    }
    return res


async def get_profile_id(db: Session, id: int):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    profile_one = query.first()

    profile_one = (
        (
            profile_one.to_dict()
            if hasattr(profile_one, "to_dict")
            else vars(profile_one)
        )
        if profile_one
        else profile_one
    )

    res = {
        "profile_one": profile_one,
    }
    return res


async def post_profile(db: Session, raw_data: schemas.PostProfile):
    id: int = raw_data.id
    name: str = raw_data.name
    address: str = raw_data.address
    mobile: str = raw_data.mobile
    password: str = raw_data.password
    email: str = raw_data.email
    amount: int = raw_data.amount
    test: str = raw_data.test
    test1: datetime.datetime = raw_data.test1
    saffds: datetime.datetime = raw_data.saffds
    gdfgdf: datetime.datetime = raw_data.gdfgdf

    record_to_be_added = {
        "id": id,
        "name": name,
        "test": test,
        "email": email,
        "test1": test1,
        "amount": amount,
        "gdfgdf": gdfgdf,
        "mobile": mobile,
        "saffds": saffds,
        "address": address,
        "password": password,
    }
    new_profile = models.Profile(**record_to_be_added)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    profile_inserted_record = new_profile.to_dict()

    res = {
        "profile_inserted_record": profile_inserted_record,
    }
    return res


async def put_profile_id(db: Session, raw_data: schemas.PutProfileId):
    id: int = raw_data.id
    name: str = raw_data.name
    address: str = raw_data.address
    mobile: str = raw_data.mobile
    password: str = raw_data.password
    email: str = raw_data.email
    amount: int = raw_data.amount
    test: str = raw_data.test
    test1: datetime.datetime = raw_data.test1
    saffds: datetime.datetime = raw_data.saffds
    gdfgdf: datetime.datetime = raw_data.gdfgdf

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))
    profile_edited_record = query.first()

    if profile_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "test": test,
            "email": email,
            "test1": test1,
            "amount": amount,
            "gdfgdf": gdfgdf,
            "mobile": mobile,
            "saffds": saffds,
            "address": address,
            "password": password,
        }.items():
            setattr(profile_edited_record, key, value)

        db.commit()
        db.refresh(profile_edited_record)

        profile_edited_record = (
            profile_edited_record.to_dict()
            if hasattr(profile_edited_record, "to_dict")
            else vars(profile_edited_record)
        )
    res = {
        "profile_edited_record": profile_edited_record,
    }
    return res


async def delete_profile_id(db: Session, raw_data: schemas.DeleteProfileId):
    id: int = raw_data.id

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        profile_deleted = record_to_delete.to_dict()
    else:
        profile_deleted = record_to_delete
    res = {
        "profile_deleted": profile_deleted,
    }
    return res


async def get_records(db: Session):

    query = db.query(models.Records)

    records_all = query.all()
    records_all = (
        [new_data.to_dict() for new_data in records_all] if records_all else records_all
    )
    res = {
        "records_all": records_all,
    }
    return res


async def get_records_id(db: Session, id: int):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    records_one = query.first()

    records_one = (
        (
            records_one.to_dict()
            if hasattr(records_one, "to_dict")
            else vars(records_one)
        )
        if records_one
        else records_one
    )

    res = {
        "records_one": records_one,
    }
    return res


async def post_records(db: Session, raw_data: schemas.PostRecords):
    id: int = raw_data.id
    username: str = raw_data.username
    address: str = raw_data.address
    pincode: str = raw_data.pincode
    user_amount: int = raw_data.user_amount

    record_to_be_added = {
        "id": id,
        "address": address,
        "pincode": pincode,
        "username": username,
        "user_amount": user_amount,
    }
    new_records = models.Records(**record_to_be_added)
    db.add(new_records)
    db.commit()
    db.refresh(new_records)
    records_inserted_record = new_records.to_dict()

    res = {
        "records_inserted_record": records_inserted_record,
    }
    return res


async def put_records_id(db: Session, raw_data: schemas.PutRecordsId):
    id: int = raw_data.id
    username: str = raw_data.username
    address: str = raw_data.address
    pincode: str = raw_data.pincode
    user_amount: int = raw_data.user_amount

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))
    records_edited_record = query.first()

    if records_edited_record:
        for key, value in {
            "id": id,
            "address": address,
            "pincode": pincode,
            "username": username,
            "user_amount": user_amount,
        }.items():
            setattr(records_edited_record, key, value)

        db.commit()
        db.refresh(records_edited_record)

        records_edited_record = (
            records_edited_record.to_dict()
            if hasattr(records_edited_record, "to_dict")
            else vars(records_edited_record)
        )
    res = {
        "records_edited_record": records_edited_record,
    }
    return res


async def delete_records_id(db: Session, raw_data: schemas.DeleteRecordsId):
    id: int = raw_data.id

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        records_deleted = record_to_delete.to_dict()
    else:
        records_deleted = record_to_delete
    res = {
        "records_deleted": records_deleted,
    }
    return res


async def put_students_id(db: Session, raw_data: schemas.PutStudentsId):
    id: int = raw_data.id
    name: str = raw_data.name
    age: str = raw_data.age

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {"id": id, "age": age, "name": name}.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_id(db: Session, raw_data: schemas.DeleteStudentsId):
    id: int = raw_data.id

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_test123456789(db: Session):

    query = db.query(models.Test123456789)

    test123456789_all = query.all()
    test123456789_all = (
        [new_data.to_dict() for new_data in test123456789_all]
        if test123456789_all
        else test123456789_all
    )
    res = {
        "test123456789_all": test123456789_all,
    }
    return res


async def get_test123456789_id(db: Session, id: int):

    query = db.query(models.Test123456789)
    query = query.filter(and_(models.Test123456789.id == id))

    test123456789_one = query.first()

    test123456789_one = (
        (
            test123456789_one.to_dict()
            if hasattr(test123456789_one, "to_dict")
            else vars(test123456789_one)
        )
        if test123456789_one
        else test123456789_one
    )

    res = {
        "test123456789_one": test123456789_one,
    }
    return res


async def post_test123456789(db: Session, raw_data: schemas.PostTest123456789):
    id: int = raw_data.id

    record_to_be_added = {"id": id}
    new_test123456789 = models.Test123456789(**record_to_be_added)
    db.add(new_test123456789)
    db.commit()
    db.refresh(new_test123456789)
    test123456789_inserted_record = new_test123456789.to_dict()

    res = {
        "test123456789_inserted_record": test123456789_inserted_record,
    }
    return res


async def put_test123456789_id(db: Session, raw_data: schemas.PutTest123456789Id):
    id: int = raw_data.id

    query = db.query(models.Test123456789)
    query = query.filter(and_(models.Test123456789.id == id))
    test123456789_edited_record = query.first()

    if test123456789_edited_record:
        for key, value in {"id": id}.items():
            setattr(test123456789_edited_record, key, value)

        db.commit()
        db.refresh(test123456789_edited_record)

        test123456789_edited_record = (
            test123456789_edited_record.to_dict()
            if hasattr(test123456789_edited_record, "to_dict")
            else vars(test123456789_edited_record)
        )
    res = {
        "test123456789_edited_record": test123456789_edited_record,
    }
    return res


async def put_trujghyr_id(db: Session, raw_data: schemas.PutTrujghyrId):
    id: int = raw_data.id
    fsg: str = raw_data.fsg

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))
    trujghyr_edited_record = query.first()

    if trujghyr_edited_record:
        for key, value in {"id": id, "fsg": fsg}.items():
            setattr(trujghyr_edited_record, key, value)

        db.commit()
        db.refresh(trujghyr_edited_record)

        trujghyr_edited_record = (
            trujghyr_edited_record.to_dict()
            if hasattr(trujghyr_edited_record, "to_dict")
            else vars(trujghyr_edited_record)
        )
    res = {
        "trujghyr_edited_record": trujghyr_edited_record,
    }
    return res


async def delete_trujghyr_id(db: Session, raw_data: schemas.DeleteTrujghyrId):
    id: int = raw_data.id

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        trujghyr_deleted = record_to_delete.to_dict()
    else:
        trujghyr_deleted = record_to_delete
    res = {
        "trujghyr_deleted": trujghyr_deleted,
    }
    return res
