from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uuid
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

from typing import Any, Optional, List
from data_models import (
    ApiGenerateNoteRequest,
    ApiGenerateNoteResponse,
    ApiSaveNoteRequest,
    ApiSaveNoteResponse,
    ApiLoadNotesRequest,
    ApiLoadNotesResponse,
    Note
)

load_dotenv()

# TODO: Integrate Langchain to optimize LLM interface
# initialize interface with OpenAI
OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=OPENAI_KEY)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOCAL_NOTES: List[Note] = []  # TODO: Move to persistent storage


@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/generate_note")
async def generate_note(req: ApiGenerateNoteRequest) -> ApiGenerateNoteResponse:
    """Generate AI notes based on therapist observations"""

    generated_note: Optional[str] = None

    # Use the input observations to generate the note
    # TODO: Improve prompt
    llm_prompt = """
        Your task is to generate note from therapist observations. 
        use a professional language, be concise and clear.
    """

    observations = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": llm_prompt},
            {"role": "user", "content": req.input_observations}
        ]
    )

    # TODO: Validate errors and use fallbacks if necessary
    generated_note = observations.choices[0].message.content

    # returns results to FE
    if generated_note:
        return ApiGenerateNoteResponse(generated_note=generated_note)
    else:
        return ApiGenerateNoteResponse(error="Failed to generate note")


@app.post("/save_note")
async def save_note(req: ApiSaveNoteRequest) -> ApiSaveNoteResponse:
    """Save therapist notes"""
    if req.note and req.therapist_id:
        LOCAL_NOTES.append(Note(
            id=str(uuid.uuid4()),
            date=int(time.time()),
            observations=req.note,
            therapist_id=req.therapist_id
        ))
        return ApiSaveNoteResponse(success=True)
    else:
        return ApiSaveNoteResponse(success=False, error="Missing note or therapist")


@app.post("/load_notes")
async def load_notes(req: ApiLoadNotesRequest) -> ApiLoadNotesResponse:
    """Load therapist notes from memory"""

    # TODO: Add filter for therapist_id and start/end time
    reversed_notes = list(reversed(LOCAL_NOTES))

    if reversed_notes:
        return ApiLoadNotesResponse(notes=reversed_notes)
    else:
        return ApiLoadNotesResponse(error="No notes found")
