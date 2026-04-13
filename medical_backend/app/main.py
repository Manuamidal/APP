from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.patient_routes import router as patient_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(patient_router)

# Run
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000