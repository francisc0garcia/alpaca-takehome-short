from pydantic import BaseModel
from typing import Any, Optional, List


class Note(BaseModel):
    id: str  # Unique ID of the note
    date: int  # seconds in epoch time
    observations: str  # Therapist notes
    therapist_id: str  # ID of the therapist


class ApiGenerateNoteRequest(BaseModel):
    input_observations: str  # Therapist notes
    duration: int  # Session duration in seconds
    type: str  # Type os session


class ApiGenerateNoteResponse(BaseModel):
    generated_note: Optional[str] = None  # AI note
    error: Optional[str] = None  # Error message


class ApiSaveNoteRequest(BaseModel):
    note: str  # Therapist notes (AI improved)
    therapist_id: str  # ID of the therapist


class ApiSaveNoteResponse(BaseModel):
    success: bool  # True if the note was saved successfully
    error: Optional[str] = None  # Error message


class ApiLoadNotesRequest(BaseModel):
    therapist_id: str  # ID of the therapist
    start_date: int  # seconds in epoch time
    end_date: int  # seconds in epoch time


class ApiLoadNotesResponse(BaseModel):
    notes: List[Note]  # List of notes
    error: Optional[str] = None  # Error message
