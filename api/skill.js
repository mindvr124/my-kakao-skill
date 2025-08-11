// Vercel 환경에서 body를 수동으로 파싱
export default function handler(req, res) {
  console.log('Request received:', req.method);
  
  if (req.method === 'GET') {
    return res.status(200).json({ status: 'OK' });
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 기본 응답 (일단 하드코딩으로 테스트)
  const response = {
    "version": "2.0",
    "template": {
      "outputs": [{
        "simpleText": {
          "text": "안녕하세요! 카카오 스킬이 정상 작동합니다."
        }
      }]
    }
  };

  console.log('Sending basic response');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  return res.status(200).json(response);
}

// body 파싱을 위한 설정
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '1mb',
    },
  },
}