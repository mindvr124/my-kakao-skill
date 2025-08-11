from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/skill")
async def skill_endpoint(request: Request):
    try:
        body = await request.json()
        user_text = body.get("userRequest", {}).get("utterance", "")
    except Exception:
        user_text = ""

    return JSONResponse(
        content={
            "version": "2.0",
            "template": {
                "outputs": [
                    {"simpleText": {"text": f"안녕하세요! '{user_text}' 라고 하셨네요."}}
                ]
            }
        },
        status_code=200,
        media_type="application/json; charset=utf-8"
    )
