from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    phone: str
    email: str
    blood_group: str
    allergies: Optional[str] = None
    last_visit: str