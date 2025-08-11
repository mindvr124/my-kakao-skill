from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/skill")
async def skill(request: Request):
    req_data = await request.json()
    utterance = req_data["userRequest"]["utterance"]
    print("사용자 발화:", utterance)

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"안녕하세요! '{utterance}' 라고 하셨네요."
                    }
                }
            ]
        }
    }
