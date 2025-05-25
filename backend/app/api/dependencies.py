from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token # Assuming verify_token is in app.core.security
# If settings are needed, e.g., for tokenUrl:
# from app.core.config import settings

# Define the OAuth2 password bearer scheme
# The tokenUrl should point to your login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login") # Adjusted tokenUrl

async def get_current_user(token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real application, you would decode the token and retrieve the user from the database.
    # For this placeholder, we'll return a dummy user dictionary.
    # You might also want to fetch user details from a database here.
    user = {"username": "dummyuser", "email": "user@example.com"} # Example user object
    return user
