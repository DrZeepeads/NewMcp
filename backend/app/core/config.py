from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Nelson-GPT Backend"
    API_V1_STR: str = "/api/v1"
    MCP_SERVER_URL: str = "http://localhost:3001/api/v1"  # Default MCP server URL

    class Config:
        env_file = ".env"
        extra = "ignore" # Allow .env file to not exist without error, useful for defaults

settings = Settings()
