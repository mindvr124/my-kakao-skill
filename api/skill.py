from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# 루트 경로에서 POST 요청 처리
@app.post("/")
async def skill_endpoint(request: Request):
    try:
        body = await request.json()
        user_text = body.get("userRequest", {}).get("utterance", "")
        
        # 디버깅용 로그 (배포 후 제거 가능)
        print(f"Received request: {json.dumps(body, ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"Error parsing request: {e}")
        user_text = ""

    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"안녕하세요! '{user_text}' 라고 하셨네요."
                    }
                }
            ]
        }
    }
    
    print(f"Sending response: {json.dumps(response_body, ensure_ascii=False, indent=2)}")

    return JSONResponse(
        content=response_body,
        status_code=200,
        headers={
            "Content-Type": "application/json; charset=utf-8"
        }
    )

# 기존 엔드포인트도 유지 (테스트용)
@app.post("/skill")
async def skill_endpoint_legacy(request: Request):
    return await skill_endpoint(request)