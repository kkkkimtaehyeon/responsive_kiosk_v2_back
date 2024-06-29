from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_= load_dotenv(find_dotenv())

cleint = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

client = OpenAI()

def openai_tts(text):
    with cleint.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text,
        response_format="opus"
    ) as stream:
        for chunk in stream.iter_bytes(chunk_size=1600):
            print(f'chunk: ${type(chunk)}, ${len(chunk)}')

openai_tts("안녕하세요. 제 이름은 김태현입니다.")