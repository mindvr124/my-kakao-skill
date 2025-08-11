module.exports = (req, res) => {
    // CORS 헤더 설정
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
  
    if (req.method === 'OPTIONS') {
      res.status(200).end();
      return;
    }
  
    if (req.method === 'GET') {
      res.status(200).json({ status: 'OK', message: 'Kakao Skill Server is running' });
      return;
    }
  
    if (req.method !== 'POST') {
      res.status(405).json({ error: 'Method not allowed' });
      return;
    }
  
    try {
      const userText = req.body?.userRequest?.utterance || '';
      
      const responseBody = {
        version: '2.0',
        template: {
          outputs: [
            {
              simpleText: {
                text: `안녕하세요! '${userText}' 라고 하셨네요.`
              }
            }
          ]
        }
      };
  
      res.status(200).json(responseBody);
    } catch (error) {
      console.error('Error:', error);
      res.status(500).json({
        version: '2.0',
        template: {
          outputs: [
            {
              simpleText: {
                text: '서버 오류가 발생했습니다.'
              }
            }
          ]
        }
      });
    }
  };