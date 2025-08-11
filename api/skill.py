from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/skill")
async def skill(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = await request.body()
        body = body.decode("utf-8")

    print("=== 📥 카카오에서 받은 요청 ===")
    print(json.dumps(body, ensure_ascii=False, indent=2))

    # 카카오 응답 포맷
    response_data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"요청 정상 수신: {body}"
                    }
                }
            ]
        }
    }
    return response_data

@app.get("/")
async def root():
    return {"status": "OK"}
