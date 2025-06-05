# app/integrations/google.py

import httpx

GOOGLE_TOKENINFO_URL = "https://oauth2.googleapis.com/tokeninfo"

async def verify_token(id_token: str) -> dict | None:
    """
    Google OAuth2 ID 토큰 검증 함수

    Args:
        id_token (str): 프론트에서 받은 Google ID 토큰

    Returns:
        dict | None: 토큰 정보가 유효하면 사용자 프로필 반환, 아니면 None
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_TOKENINFO_URL, params={"id_token": id_token})

    if response.status_code == 200:
        return response.json()
    return None
