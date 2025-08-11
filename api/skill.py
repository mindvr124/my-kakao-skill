from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"status": "OK", "message": "Skill server is running"}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        try:
            # 요청 본문 읽기
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                post_data = self.rfile.read(content_length)
                body = json.loads(post_data.decode('utf-8'))
                user_text = body.get("userRequest", {}).get("utterance", "")
            else:
                user_text = ""

            # 응답 생성
            response_data = {
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

            # 응답 전송
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))

        except Exception as e:
            print(f"Error: {e}")
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            error_response = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "서버 오류가 발생했습니다."
                            }
                        }
                    ]
                }
            }
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))