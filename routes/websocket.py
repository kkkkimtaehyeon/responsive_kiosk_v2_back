from fastapi import WebSocket, APIRouter
import json
router = APIRouter()

gpt_general_response = {
            "isMenu": False,
            "isOrder": False,
            "isAnswer": True,
            "content": {
                "answer": "gpt의 답변 예시입니다.",
                "menus": {}
            }
        }




@router.websocket("/conversations")
async def conversation(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            text = await websocket.receive_text()
            print(text)
            
            #gpt 로직 추가
            gpt_response = {
                "isMenu": True,
                "isOrder": False,
                "isAnswer": True,
                "content": {
                    "answer": "아메리카노를 추가하셨습니다.",
                    "menus": {
                            "id": 1,
                            "name": "아메리카노",
                            "price": 3000,
                            "amount": 1,
                        }
                }
            }
            #response = validateResponse(gpt_response)
            await websocket.send_json(gpt_response)
            print(gpt_response)
            
    except Exception as e:
        print(e)
        print('음성인식 종료')

def validateResponse(response):
    # 메뉴 추가
    if response["isOrder"]:
        return response["content"]
    # gpt 답변
    else:
        return response["content"]["script"]
    


