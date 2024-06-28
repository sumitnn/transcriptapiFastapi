from pydantic import BaseModel

class TranscriptionSchema(BaseModel):
    transcript: str
