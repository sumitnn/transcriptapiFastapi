import os
import subprocess
import uuid
import speech_recognition as sr
from fastapi import UploadFile

class AudioProcessor:
    def __init__(self, audio_file: UploadFile):
        self.audio_file = audio_file
        self.output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wav_files')
        self.unique_id = str(uuid.uuid4())[:8]
        self.wav_file_path = os.path.join(self.output_folder, f'converted_wav_file_{self.unique_id}.wav')
        self.temp_audio_path = os.path.join(self.output_folder, f'temp_audio_file_{self.unique_id}')
        self.transcription = None

    def save_temp_audio_file(self):
        with open(self.temp_audio_path, 'wb') as temp_file:
            temp_file.write(self.audio_file.file.read())

    def convert_to_wav(self):
        try:
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
            
            ffmpeg_path = "ffmpeg"  
            
            self.save_temp_audio_file()
            subprocess.call([ffmpeg_path, '-i', self.temp_audio_path, self.wav_file_path])
        except Exception as e:
            print(e)
        finally:
            if os.path.exists(self.temp_audio_path):
                os.remove(self.temp_audio_path)

    def generate_transcription(self):
        recognizer = sr.Recognizer()

        with sr.AudioFile(self.wav_file_path) as source:
            audio = recognizer.record(source)

            try:
                self.transcription = recognizer.recognize_google(audio)
            except Exception as e:
                print("error in generate transcription",e)
           

        self.delete_wav_file()
        if self.transcription:
            return self.transcription
        return None

    def delete_wav_file(self):
        try:
            os.remove(self.wav_file_path)
            print(f"File '{self.wav_file_path}' deleted.")
        except Exception as e:
            print(f"Error deleting file '{self.wav_file_path}': {e}")

