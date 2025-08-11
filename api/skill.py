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

    return JSONResponse(
        content=response_body,
        status_code=200,
        headers={"Content-Type": "application/json;charset=UTF-8"}
    )
