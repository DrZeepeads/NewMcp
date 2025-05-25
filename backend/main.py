from fastapi import FastAPI

app = FastAPI(title="Nelson-GPT Backend")

@app.get("/")
async def root():
    return {"message": "Welcome to Nelson-GPT Backend"}

# Include routers from app.api.routes
# from app.api.routes import chat, auth # Example
# app.include_router(chat.router, prefix="/api")
# app.include_router(auth.router, prefix="/api/auth")
