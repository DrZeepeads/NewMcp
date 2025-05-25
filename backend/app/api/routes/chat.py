from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.models.chat import ChatRequest, ChatResponse
# from app.api.dependencies import get_current_user # Assuming a dependency for current user
from app.services.nelson_mcp_client import NelsonMCPClient # Import the MCP client
import logging

# Configure logging if not already configured broadly
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
mcp_client = NelsonMCPClient() # Initialize the client (uses default URL from settings)

# Placeholder function for background task
def summarize_conversation(query: str, response_answer: str):
    logger.info(f"BG Task: Summarizing conversation for query: '{query}' and response: '{response_answer[:50]}...'")
    # In a real scenario, this would involve more complex logic,
    # like calling another service, storing data, etc.
    # For now, just a log message.
    pass

@router.post("/ask", response_model=ChatResponse)
async def ask_question(
    request: ChatRequest,
    background_tasks: BackgroundTasks, # Add BackgroundTasks parameter
    # current_user: dict = Depends(get_current_user) # Example of protecting endpoint
):
    """
    Receives a question, forwards it to the MCP server via NelsonMCPClient,
    and returns the processed answer.
    """
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    mcp_response = await mcp_client.search_documents(request.query)

    if mcp_response.get("error"):
        # If MCP client returned an error structure
        status_code = mcp_response.get("status_code", 500)
        detail = mcp_response.get("detail", "Error communicating with MCP server.")
        raise HTTPException(status_code=status_code, detail=detail)

    # Assuming MCP response has a 'results' list, and each item has 'content'
    # For this placeholder flow, we'll take the content of the first result as the answer.
    # This structure depends on mcp-server/tools/vector_search.js mock response.
    # The mock response is: { results: [ { id: "doc1", content: "...", ... }, ... ] }
    
    first_result_content = "No relevant documents found." # Default if no results
    citations_list = []

    if mcp_response.get("results") and len(mcp_response["results"]) > 0:
        first_result = mcp_response["results"][0]
        first_result_content = first_result.get("content", "Content not available.")
        # Example of creating a simple citation string
        citations_list.append(f"Source: {first_result.get('metadata', {}).get('source', 'Unknown')}, ID: {first_result.get('id', 'N/A')}")

    chat_response = ChatResponse(answer=first_result_content, citations=citations_list)

    # Add the background task
    background_tasks.add_task(summarize_conversation, request.query, chat_response.answer)
    logger.info("Added summarize_conversation to background tasks.")

    return chat_response
