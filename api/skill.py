from fastapi import FastAPI, Request, Response
import json

app = FastAPI()

@app.post("/api/skill")
async def skill_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    user_text = (body.get("userRequest") or {}).get("utterance") or ""

    resp = {
        "version": "2.0",
        "template": {
            "outputs": [
                {"simpleText": {"text": f"안녕하세요! '{user_text}' 라고 하셨네요."}}
            ]
        }
    }

    # 카카오 호환: application/json (charset 제거), 공백 없는 JSON
    payload = json.dumps(resp, ensure_ascii=False, separators=(',', ':'))
    return Response(content=payload, media_type="application/json", status_code=200)
