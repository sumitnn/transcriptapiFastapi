##Audio Transcription Backend with FastAPI
This project implements a FastAPI-based backend for audio transcription, utilizing OAuth2 JWT authentication, and MongoDB for data storage.

Getting Started
To get this project up and running, follow these steps:

Prerequisites
Python: Ensure Python 3.7+ is installed on your system.
ffmpeg: Install ffmpeg for audio file processing

Setup
Clone the repository:
git clone this repo
cd <repository_name>

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
install dependency
pip install -r requirements.txt

run mongo db locally

run fastapi server 
uvicorn main:app --port 8000 --reload

Authentication
Obtain a JWT token for authentication
GET http://127.0.0.1:8000/token?username=test&password=password

Transcription API Endpoint
Upload an audio file for transcription
POST http://127.0.0.1:8000/transcribe
Content-Type: multipart/form-data
Authorization: Bearer <token>

api swagger link
http://127.0.0.1:8000/docs

note:
mongo db is running locally and ffmpeg installed in a system


