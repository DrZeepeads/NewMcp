import httpx
import logging
from typing import Dict, Any
from app.core.config import settings # To get MCP_SERVER_URL

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NelsonMCPClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or settings.MCP_SERVER_URL
        # Ensure the base_url for MCP ends with /api/v1 if that's where endpoints are mounted
        if not self.base_url.endswith('/api/v1'):
             # Basic check, adjust if MCP server structure is different
            if self.base_url.endswith('/'):
                self.base_url += 'api/v1'
            else:
                self.base_url += '/api/v1'


    async def search_documents(self, query: str) -> Dict[str, Any]:
        """
        Calls the MCP server's /vector/search endpoint.
        """
        search_url = f"{self.base_url}/vector/search"
        logger.info(f"Contacting MCP server at {search_url} with query: '{query}'")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    search_url,
                    json={"query": query},
                    timeout=10.0 # seconds
                )
                response.raise_for_status() # Raises an HTTPStatusError for 4XX/5XX responses
                
                data = response.json()
                logger.info(f"Received response from MCP server: {data}")
                return data
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error occurred while contacting MCP server: {e.response.status_code} - {e.response.text}")
                # Return a structured error or raise a custom exception
                return {"error": True, "status_code": e.response.status_code, "detail": e.response.text}
            except httpx.RequestError as e:
                logger.error(f"Request error occurred while contacting MCP server: {e}")
                return {"error": True, "status_code": 500, "detail": f"MCP connection error: {str(e)}"}
            except Exception as e:
                logger.error(f"An unexpected error occurred in MCP client: {e}")
                return {"error": True, "status_code": 500, "detail": f"Unexpected error: {str(e)}"}

# Example of how to use the client (optional, for testing or direct use)
# async def main():
#     client = NelsonMCPClient()
#     results = await client.search_documents("common cold symptoms")
#     print("Search results:", results)

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
