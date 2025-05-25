import React, { useState } from 'react';
import { askQuery } from '../api/chat'; // Import the updated askQuery

function ChatInterface() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!query.trim()) return;

    setIsLoading(true);
    setResponse('');
    setError('');

    try {
      const result = await askQuery(query);
      // Assuming the backend response structure is { answer: "...", citations: [...] }
      // And the MCP client will pass through the 'content' as 'answer'
      setResponse(result.answer || 'No answer text found in response.');
      // Later, you might want to display citations: result.citations
      console.log('Citations received:', result.citations);
    } catch (err) {
      console.error('Error submitting query:', err);
      setError(err.message || 'Failed to fetch response from the server.');
    } finally {
      setIsLoading(false);
      // setQuery(''); // Optionally clear input after sending
    }
  };

  return (
    <div>
      <h2>Chat with Nelson-GPT</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
          disabled={isLoading}
          style={{ width: '80%', padding: '10px', marginRight: '10px' }}
        />
        <button type="submit" disabled={isLoading} style={{ padding: '10px' }}>
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>
      {isLoading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {response && (
        <div>
          <p><strong>Answer:</strong> {response}</p>
        </div>
      )}
      {!isLoading && !response && !error && <p>Ask a question to get a response.</p>}
    </div>
  );
}

export default ChatInterface;
