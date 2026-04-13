from app.models.patient import Patient

patients_db = {
    1: Patient(
        id=1,
        name="Rahul Sharma",
        age=28,
        gender="Male",
        phone="+91-9876543210",
        email="rahul@gmail.com",
        blood_group="O+",
        allergies="None",
        last_visit="2026-04-01"
    ),
    2: Patient(
        id=2,
        name="Priya Patel",
        age=32,
        gender="Female",
        phone="+91-9876543211",
        email="priya@gmail.com",
        blood_group="B+",
        allergies="None",
        last_visit="2026-04-01"
    )
}