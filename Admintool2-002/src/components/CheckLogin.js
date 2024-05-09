import React, { useState } from 'react';
import axios from 'axios';

function CheckLogin() {
  const [statusCheck, setStatusCheck] = useState('');
  const [loadingCheck, setLoadingCheck] = useState(false);

  const checkLoginStatus = async () => {
    setLoadingCheck(true);
    try {
      const result = await axios.post('http://localhost:5000/check_login');
      setStatusCheck(result.data.status);
    } catch (error) {
      console.error("Error: ", error.response ? error.response.data : error);
      setStatusCheck(`Error: ${error.message}`);
    }
    setLoadingCheck(false);
  };

  return (
    <div className="App">
      <button onClick={checkLoginStatus} disabled={loadingCheck}>
        {loadingCheck ? 'Loading...' : 'Check Login'}
      </button>
      <p>{statusCheck}</p>
    </div>
  );
}

export default CheckLogin;
