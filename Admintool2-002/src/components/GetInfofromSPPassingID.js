import React, { useState } from 'react';
import CryptoJS from 'crypto-js';

const GetInfofromSPPassingID = () => {
    const [userID, setUserID] = useState("");
    const [loadingCheck, setLoadingCheck] = useState(false);
    const [statusCheck, setStatusCheck] = useState(null);

    const checkLoginStatus = async (e) => {
        e.preventDefault();
        setLoadingCheck(true);

        var key = CryptoJS.enc.Utf8.parse(process.env.REACT_APP_SECRET_KEY);

        var encryptedUserID = CryptoJS.AES.encrypt(userID, key, {mode: CryptoJS.mode.ECB});
        encryptedUserID = encryptedUserID.toString();
        console.log('encrypted', encryptedUserID );

        const response = await fetch('http://localhost:5000/getInfofromSPPassingID', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ID: encryptedUserID }),
        });

        const data = await response.json();
        setStatusCheck(data.status);
        setLoadingCheck(false);
    };

    return (
        <form onSubmit={checkLoginStatus}>
            <input type="email" value={userID} onChange={(e) => setUserID(e.target.value)} placeholder="UserID" required />
            <button type="submit">Get User Info From SP</button>
        </form>
    );
};

export default GetInfofromSPPassingID;
