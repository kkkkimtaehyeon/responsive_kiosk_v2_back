from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
# 청크 단위를 파일로 변환 -> 바로 whisper에게 넘겨줌

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key= OPENAI_API_KEY)

audio_file= open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
    file="webm",
    model="whisper-1", 
    file=audio_file
)
print(transcription.text)