from fastapi import FastAPI, UploadFile, File, HTTPException, Depends

from app.auth import get_current_user, create_access_token
from app.database import collection
from app.auth import TokenData
from app.speechtotext import AudioProcessor


app = FastAPI()



@app.post("/token")
async def login(username: str, password: str):
    # dummy user
    if username == "test" and password == "password":
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...), current_user: TokenData = Depends(get_current_user)):
    processor = AudioProcessor(file)
    processor.convert_to_wav()
    transcription = processor.generate_transcription()
    if transcription:

        collection.insert_one({"ts":transcription})
        return {"transcript": transcription}
    else:
        raise HTTPException(status_code=400, detail="Transcription failed")
    


