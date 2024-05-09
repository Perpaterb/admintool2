import React, { useState } from 'react';
import axios from 'axios';

function OpenLoginUTS() {
  const [statusOpen, setStatusOpen] = useState('');
  const [loadingOpen, setLoadingOpen] = useState(false);

  const handleOpenAlert = async () => {
    setLoadingOpen(true);
    try {
      const result = await axios.post('http://localhost:5000/open_or_alert');
      setStatusOpen(result.data.status);
    } catch (error) {
      console.error("Error: ", error.response ? error.response.data : error);
      setStatusOpen(`Error: ${error.message}`);
    }
    setLoadingOpen(false);
  }; 

  return (
    <div className="App">
      <button onClick={handleOpenAlert} disabled={loadingOpen}>
        {loadingOpen ? 'Loading...' : 'Open or Alert'}
      </button>
      <p>{statusOpen}</p>
    </div>
  );
}

export default OpenLoginUTS;
