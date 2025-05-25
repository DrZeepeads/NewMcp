import React from 'react';
// import './App.css'; // Assuming a basic App.css might exist or be created later
import ChatInterface from './components/ChatInterface'; // Import the ChatInterface

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Nelson-GPT</h1>
      </header>
      <main>
        <ChatInterface />
      </main>
    </div>
  );
}

export default App;
