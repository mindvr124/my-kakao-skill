export default async function handler(req, res) {
  console.log('=== Kakao Skill Request ===');
  console.log('Method:', req.method);
  console.log('Headers:', req.headers);
  console.log('Raw Body:', req.body);

  if (req.method === 'GET') {
    return res.status(200).json({ 
      message: 'Kakao Skill Server is running',
      status: 'OK',
      timestamp: new Date().toISOString()
    });
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // POST 요청 처리
  let userText = 'Unknown';
  let requestBody = null;
  
  try {
    // 요청 본문 처리 - 여러 방법 시도
    if (req.body) {
      if (typeof req.body === 'string') {
        requestBody = JSON.parse(req.body);
      } else {
        requestBody = req.body;
      }
    }
    
    console.log('Parsed Body:', requestBody);
    
    if (requestBody && requestBody.userRequest) {
      userText = requestBody.userRequest.utterance || 'No utterance';
    } else {
      userText = 'No userRequest found';
    }
    
  } catch (error) {
    console.error('Error processing request:', error);
    userText = `Error: ${error.message}`;
  }

  // 카카오 챗봇 응답 형식
  const response = {
    "version": "2.0",
    "template": {
      "outputs": [{
        "simpleText": {
          "text": `안녕하세요! '${userText}' 라고 하셨네요.`
        }
      }]
    }
  };

  console.log('Sending Response:', JSON.stringify(response, null, 2));
  
  // 응답 헤더 설정
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  return res.status(200).json(response);
}