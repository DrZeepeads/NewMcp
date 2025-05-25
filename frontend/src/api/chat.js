/**
 * Makes an API call to the backend to ask a question.
 *
 * @param {string} query The question to ask.
 * @returns {Promise<object>} A promise that resolves to the API response.
 * @throws {Error} If the API request fails.
 */
export async function askQuery(query) {
  console.log('[API] Sending query to backend:', query);
  const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000/api/v1/chat/ask';

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query: query }),
    });

    if (!response.ok) {
      // Attempt to read the error response body
      let errorData;
      try {
        errorData = await response.json();
      } catch (e) {
        // If response body is not JSON or empty
        errorData = { message: response.statusText };
      }
      console.error('[API] Backend request failed:', response.status, errorData);
      throw new Error(`API request failed with status ${response.status}: ${errorData.detail || errorData.message}`);
    }

    const data = await response.json();
    console.log('[API] Received response from backend:', data);
    return data;
  } catch (error) {
    console.error('[API] Error during fetch operation:', error);
    // Re-throw the error so it can be caught by the calling component
    throw error;
  }
}
