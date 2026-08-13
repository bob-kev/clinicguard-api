from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# Base Patient schema with shared properties
class PatientBase(SQLModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    date_of_birth: datetime
    phone: str = Field(index=True)
    email: Optional[str] = None
    address: Optional[str] = None
    medical_notes: Optional[str] = None
    doctor_id: Optional[int] = Field(default=None, foreign_key="user.id")

# Database Table Model
class Patient(PatientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_by: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Explicit foreign_keys configuration to resolve AmbiguousForeignKeysError
    doctor: Optional["User"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Patient.doctor_id]"}
    )

# Schema for Creating a Patient
class PatientCreate(PatientBase):
    pass

# Schema for Updating a Patient
class PatientUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    medical_notes: Optional[str] = None
    doctor_id: Optional[int] = None