from fastapi import WebSocket, APIRouter, WebSocketException, WebSocketDisconnect
from openai import OpenAI
import os
import io
from dotenv import load_dotenv, find_dotenv
from DB.schemas import MenuService
from DB.dummy_datas import DUMMY_ANSWER_CART_DATA

_= load_dotenv(find_dotenv())
menu_service = MenuService()

router = APIRouter()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



@router.websocket("/conversations")
async def conversation(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            text = await websocket.receive_text()
            try:
                # gpt 로직 추가
                gpt_response = DUMMY_ANSWER_CART_DATA

                if gpt_response["isAnswer"]:
                    answer = gpt_response["content"]["answer"]
                    audio_buffer = await openai_tts(answer)
                    await websocket.send_bytes(audio_buffer)

                if gpt_response["isMenu"]:
                    menu_id = gpt_response["content"]["menus"]["id"]

                    await validate_menu(id=menu_id)

                await websocket.send_json(gpt_response)
                
            except Exception as e:
                print('에러 발생', e)

    except WebSocketDisconnect:
        print('연결 종료')
    except WebSocketException:
        print('웹소켓 에러')        
            
async def validate_menu(id: str) -> bool:
    try:
        menu_service.fetch_menu(id)
        print('메뉴 있음')
        pass
    except Exception as e:
        print('메뉴 없음', e)


async def openai_tts(text):
    buffer=io.BytesIO()
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text,
        response_format="opus"
    ) as stream:
        for chunk in stream.iter_bytes(chunk_size=1600):
            buffer.write(chunk)
    
    buffer.seek(0)
    return buffer.read()  
