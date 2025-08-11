export default function handler(req, res) {
    console.log('=== Request Info ===');
    console.log('Method:', req.method);
    console.log('Headers:', req.headers);
    console.log('Body:', req.body);
    console.log('==================');
  
    // CORS 헤더
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
    if (req.method === 'OPTIONS') {
      return res.status(200).end();
    }
  
    if (req.method === 'GET') {
      return res.status(200).json({ 
        status: 'OK', 
        message: 'Kakao Skill Server is running',
        timestamp: new Date().toISOString()
      });
    }
  
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  
    // POST 요청 처리
    let userText = 'Unknown';
    
    try {
      if (req.body && typeof req.body === 'object') {
        userText = req.body.userRequest?.utterance || 'No utterance found';
      } else {
        userText = 'Invalid request body';
      }
    } catch (error) {
      console.error('Error processing request:', error);
      userText = 'Processing error';
    }
  
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
  
    console.log('Response:', JSON.stringify(response, null, 2));
    
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    return res.status(200).json(response);
  }