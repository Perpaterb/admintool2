import React, { useState } from 'react';

const OpenSP = () => {
    const [userID, setUserID] = useState("");
    const [loadingCheck, setLoadingCheck] = useState(false);
    const [statusCheck, setStatusCheck] = useState(null);

    const checkLoginStatus = async (e) => {
        e.preventDefault();
        setLoadingCheck(true);

        const response = await fetch('http://localhost:5000/open_sp', {
            method: 'POST',
            timeout: 30000,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userID}),
        });

        const data = await response.json();
        setStatusCheck(data.status);
        setLoadingCheck(false);
    };

    return (
        <div className="OpenSP">
        <input type="userID" value={userID} onChange={(e) => setUserID(e.target.value)} placeholder="User ID" required />
        <button onClick={checkLoginStatus} isabled={loadingCheck}>
          {loadingCheck ? 'Loading...' : 'Open SailPoint'}
        </button>
        <p>{statusCheck}</p>
      </div>
    );
};

export default OpenSP;
