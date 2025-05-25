const express = require('express');
const { search } = require('./tools/vector_search'); // Assuming vector_search.js is in tools directory

const app = express();
const PORT = process.env.MCP_PORT || 3001;

app.use(express.json()); // Middleware to parse JSON bodies

// API endpoint for vector search
app.post('/api/v1/vector/search', async (req, res, next) => {
    const { query } = req.body;
    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    try {
        console.log(`Received search query: ${query}`);
        const searchResults = await search(query);
        res.json(searchResults);
    } catch (error) {
        next(error); // Pass errors to the error handling middleware
    }
});

// Basic error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!', details: err.message });
});

app.listen(PORT, () => {
    console.log(`MCP Server listening on port ${PORT}`);
});
