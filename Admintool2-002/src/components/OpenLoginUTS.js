import React, { useState } from 'react';
// import axios from 'axios';

function OpenLoginUTS() {
  const [statusOpen, setStatusOpen] = useState('');
  const [loadingOpen, setLoadingOpen] = useState(false);

  const handleOpenAlert = async () => {
    setLoadingOpen(true);
    try {
      const response = await fetch('http://localhost:5000/open_or_alert', {
        method: 'POST',
        timeout: 5000
      });
      console.log("open or alert result", response);
  
      const data = await response.json();
      setStatusOpen(data.status);
    } catch (error) {
      console.error("Error: ", error.response ? error.response.data : error);
      setStatusOpen(`Error: ${error}`);
    }
    setLoadingOpen(false);
  };

  return (
    <div className="App">
      <button onClick={handleOpenAlert} disabled={loadingOpen}>
        {loadingOpen ? 'Loading...' : 'Open or Alert'}
      </button>
    </div>
  );
}

export default OpenLoginUTS;
