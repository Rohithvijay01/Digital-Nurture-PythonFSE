from pydantic import BaseModel
from typing import Optional, List

# Step 58
class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

# Step 58
class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy ORM models

# Step 59
class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True