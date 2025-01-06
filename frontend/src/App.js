// frontend/src/App.js

import React, { useState } from 'react';
import './styles.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = () => {
    fetch('/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: query }),
    })
      .then(response => response.json())
      .then(data => setResults(data.entities));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Knowledge Graph Search Engine</h1>
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Enter your query"
        />
        <button onClick={handleSearch}>Search</button>
        <ul>
          {results.map((entity, index) => (
            <li key={index}>{entity[0]} ({entity[1]})</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;