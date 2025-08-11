from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/skill")
async def basic(request: Request):
    req_data = await request.json()
    utterance =  req_data['userRequest']['utterance']
    print(utterance)
    return {"content": "안녕"}
