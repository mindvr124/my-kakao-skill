from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def ping():
    return {"ok": True, "where": "/api/skill"}

@app.post("/")
async def skill(request: Request):
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
    return JSONResponse(
        content=resp,
        media_type="application/json;charset=UTF-8",  # 공백 없이
        status_code=200
    )
