from fastapi import APIRouter, HTTPException
from app.database.db import patients_db

router = APIRouter()

@router.get("/patients/{patient_id}")
async def get_patient(patient_id: int):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients_db[patient_id]