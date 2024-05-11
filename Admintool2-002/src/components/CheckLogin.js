import React, { useState } from 'react';
// import axios from 'axios';

function CheckLogin() {
  const [statusCheck, setStatusCheck] = useState('');
  const [loadingCheck, setLoadingCheck] = useState(false);

  const checkLoginStatus = async () => {
    setLoadingCheck(true);
    const response = await fetch('http://localhost:5000/check_login', {
      method: 'POST',
      timeout: 5000
    });
    const data = await response.json();
    setStatusCheck(data.status);
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


// const checkLoginStatus = async () => {
//   setLoadingCheck(true);
//   try {
//     const result = await axios.post('http://localhost:5000/check_login',{timeout: 5000});
//     setStatusCheck(result.data.status);
//   } catch (error) {
//     console.error("Error: ", error.response ? error.response.data : error);
//     setStatusCheck(`Error: ${error}`);
//   }
//   setLoadingCheck(false);
// };