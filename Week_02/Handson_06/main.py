from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from database import engine, Base, get_db
import models, schemas

app = FastAPI(title='Course Management API', version='1.0')

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get('/')
def root():
    return {'message': 'API running'}

@app.post('/api/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = models.Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.get('/api/courses/', response_model=List[schemas.CourseResponse])
async def get_courses(
    skip: int = 0, 
    limit: int = 10, 
    department_id: Optional[int] = None, 
    db: AsyncSession = Depends(get_db)
):
    query = select(models.Course)
    if department_id:
        query = query.filter(models.Course.department_id == department_id)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    courses = result.scalars().all()
    return courses

@app.get('/api/courses/{course_id}', response_model=schemas.CourseResponse)
async def get_course_detail(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course