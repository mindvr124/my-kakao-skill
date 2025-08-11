def do_POST(self):
    try:
        # Content-Length 안전 처리
        length_header = self.headers.get('Content-Length')
        try:
            content_length = int(length_header) if length_header else 0
        except (TypeError, ValueError):
            content_length = 0

        raw = self.rfile.read(content_length) if content_length > 0 else b""
        body = {}
        if raw:
            try:
                body = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                body = {}

        user_text = body.get("userRequest", {}).get("utterance", "") or ""

        response_data = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {"simpleText": {"text": f"안녕하세요! '{user_text}' 라고 하셨네요."}}
                ]
            }
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json;charset=UTF-8")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")
        self.send_response(200)  # 카카오는 200이 아니면 바로 실패 처리
        self.send_header("Content-Type", "application/json;charset=UTF-8")
        self.end_headers()
        error_response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {"simpleText": {"text": "죄송합니다. 일시적인 오류가 발생했어요."}}
                ]
            }
        }
        self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode("utf-8"))
