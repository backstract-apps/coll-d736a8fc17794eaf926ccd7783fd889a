from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/class/')
async def get_class(db: Session = Depends(get_db)):
    try:
        return await service.get_class(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/id')
async def get_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/class/')
async def post_class(raw_data: schemas.PostClass, db: Session = Depends(get_db)):
    try:
        return await service.post_class(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/trujghyr/id')
async def get_trujghyr_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_trujghyr_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/class/id/')
async def put_class_id(raw_data: schemas.PutClassId, db: Session = Depends(get_db)):
    try:
        return await service.put_class_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/class/id')
async def delete_class_id(raw_data: schemas.DeleteClassId, db: Session = Depends(get_db)):
    try:
        return await service.delete_class_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/shivam/')
async def get_shivam(db: Session = Depends(get_db)):
    try:
        return await service.get_shivam(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/shivam/id')
async def get_shivam_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_shivam_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/shivam/')
async def post_shivam(raw_data: schemas.PostShivam, db: Session = Depends(get_db)):
    try:
        return await service.post_shivam(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/shivam/id/')
async def put_shivam_id(raw_data: schemas.PutShivamId, db: Session = Depends(get_db)):
    try:
        return await service.put_shivam_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/shivam/id')
async def delete_shivam_id(raw_data: schemas.DeleteShivamId, db: Session = Depends(get_db)):
    try:
        return await service.delete_shivam_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123/')
async def get_test123(db: Session = Depends(get_db)):
    try:
        return await service.get_test123(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123/id')
async def get_test123_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test123_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test123/')
async def post_test123(raw_data: schemas.PostTest123, db: Session = Depends(get_db)):
    try:
        return await service.post_test123(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test123/id/')
async def put_test123_id(raw_data: schemas.PutTest123Id, db: Session = Depends(get_db)):
    try:
        return await service.put_test123_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test123/id')
async def delete_test123_id(raw_data: schemas.DeleteTest123Id, db: Session = Depends(get_db)):
    try:
        return await service.delete_test123_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/')
async def get_test(db: Session = Depends(get_db)):
    try:
        return await service.get_test(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/id')
async def get_test_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test/')
async def post_test(raw_data: schemas.PostTest, db: Session = Depends(get_db)):
    try:
        return await service.post_test(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test/id/')
async def put_test_id(raw_data: schemas.PutTestId, db: Session = Depends(get_db)):
    try:
        return await service.put_test_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test/id')
async def delete_test_id(raw_data: schemas.DeleteTestId, db: Session = Depends(get_db)):
    try:
        return await service.delete_test_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/keshav/')
async def get_keshav(db: Session = Depends(get_db)):
    try:
        return await service.get_keshav(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/keshav/id')
async def get_keshav_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_keshav_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/keshav/')
async def post_keshav(raw_data: schemas.PostKeshav, db: Session = Depends(get_db)):
    try:
        return await service.post_keshav(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/keshav/id/')
async def put_keshav_id(raw_data: schemas.PutKeshavId, db: Session = Depends(get_db)):
    try:
        return await service.put_keshav_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/keshav/id')
async def delete_keshav_id(raw_data: schemas.DeleteKeshavId, db: Session = Depends(get_db)):
    try:
        return await service.delete_keshav_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/trujghyr/')
async def post_trujghyr(raw_data: schemas.PostTrujghyr, db: Session = Depends(get_db)):
    try:
        return await service.post_trujghyr(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test123456789/id')
async def delete_test123456789_id(raw_data: schemas.DeleteTest123456789Id, db: Session = Depends(get_db)):
    try:
        return await service.delete_test123456789_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/trujghyr/')
async def get_trujghyr(db: Session = Depends(get_db)):
    try:
        return await service.get_trujghyr(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(raw_data: schemas.DeleteUsersId, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test45756765/')
async def get_test45756765(db: Session = Depends(get_db)):
    try:
        return await service.get_test45756765(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test45756765/id')
async def get_test45756765_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test45756765_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test45756765/')
async def post_test45756765(raw_data: schemas.PostTest45756765, db: Session = Depends(get_db)):
    try:
        return await service.post_test45756765(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test45756765/id/')
async def put_test45756765_id(raw_data: schemas.PutTest45756765Id, db: Session = Depends(get_db)):
    try:
        return await service.put_test45756765_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test45756765/id')
async def delete_test45756765_id(raw_data: schemas.DeleteTest45756765Id, db: Session = Depends(get_db)):
    try:
        return await service.delete_test45756765_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test1234/')
async def get_test1234(db: Session = Depends(get_db)):
    try:
        return await service.get_test1234(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test1234/id')
async def get_test1234_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test1234_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test1234/')
async def post_test1234(raw_data: schemas.PostTest1234, db: Session = Depends(get_db)):
    try:
        return await service.post_test1234(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test1234/id/')
async def put_test1234_id(raw_data: schemas.PutTest1234Id, db: Session = Depends(get_db)):
    try:
        return await service.put_test1234_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test1234/id')
async def delete_test1234_id(raw_data: schemas.DeleteTest1234Id, db: Session = Depends(get_db)):
    try:
        return await service.delete_test1234_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/')
async def get_profile(db: Session = Depends(get_db)):
    try:
        return await service.get_profile(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/id')
async def get_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profile/')
async def post_profile(raw_data: schemas.PostProfile, db: Session = Depends(get_db)):
    try:
        return await service.post_profile(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profile/id/')
async def put_profile_id(raw_data: schemas.PutProfileId, db: Session = Depends(get_db)):
    try:
        return await service.put_profile_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profile/id')
async def delete_profile_id(raw_data: schemas.DeleteProfileId, db: Session = Depends(get_db)):
    try:
        return await service.delete_profile_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/')
async def get_records(db: Session = Depends(get_db)):
    try:
        return await service.get_records(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/id')
async def get_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/records/')
async def post_records(raw_data: schemas.PostRecords, db: Session = Depends(get_db)):
    try:
        return await service.post_records(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/records/id/')
async def put_records_id(raw_data: schemas.PutRecordsId, db: Session = Depends(get_db)):
    try:
        return await service.put_records_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/records/id')
async def delete_records_id(raw_data: schemas.DeleteRecordsId, db: Session = Depends(get_db)):
    try:
        return await service.delete_records_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(raw_data: schemas.PutStudentsId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(raw_data: schemas.DeleteStudentsId, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123456789/')
async def get_test123456789(db: Session = Depends(get_db)):
    try:
        return await service.get_test123456789(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123456789/id')
async def get_test123456789_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test123456789_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test123456789/')
async def post_test123456789(raw_data: schemas.PostTest123456789, db: Session = Depends(get_db)):
    try:
        return await service.post_test123456789(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test123456789/id/')
async def put_test123456789_id(raw_data: schemas.PutTest123456789Id, db: Session = Depends(get_db)):
    try:
        return await service.put_test123456789_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/trujghyr/id/')
async def put_trujghyr_id(raw_data: schemas.PutTrujghyrId, db: Session = Depends(get_db)):
    try:
        return await service.put_trujghyr_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/trujghyr/id')
async def delete_trujghyr_id(raw_data: schemas.DeleteTrujghyrId, db: Session = Depends(get_db)):
    try:
        return await service.delete_trujghyr_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

