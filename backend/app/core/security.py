from datetime import datetime, timedelta, timezone
from typing import Optional

# This is a placeholder SECRET_KEY. In a real application, this should be
# a strong, randomly generated string and kept secret.
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # In a real application, you would use a library like python-jose to encode the JWT
    # For this placeholder, we'll just return a dummy string.
    return f"dummy_jwt_token_for_{data.get('sub', 'unknown_user')}"

def verify_token(token: str) -> bool:
    # In a real application, you would use a library like python-jose to decode and verify the JWT.
    # This placeholder function will consider any token starting with "dummy_jwt_token_for_" as valid.
    return token.startswith("dummy_jwt_token_for_")
