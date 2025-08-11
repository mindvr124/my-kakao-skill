# api/skill.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

async def _skill_handler(request: Request):
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
        media_type="application/json;charset=UTF-8",
        status_code=200
    )

# POST 라우트 3개 다 열어둠 (vercel 라우팅 어디로 들어와도 OK)
app.add_api_route("/", _skill_handler, methods=["POST"])
app.add_api_route("/skill", _skill_handler, methods=["POST"])
app.add_api_route("/api/skill", _skill_handler, methods=["POST"])

# 헬스체크 (GET)
@app.get("/")
def health():
    return {"ok": True, "paths": ["/", "/skill", "/api/skill"]}
