import React, { useState } from 'react';
import CryptoJS from 'crypto-js';

const LoginComponent = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loadingCheck, setLoadingCheck] = useState(false);
    const [statusCheck, setStatusCheck] = useState(null);

    const checkLoginStatus = async (e) => {
        e.preventDefault();
        setLoadingCheck(true);

        var key = CryptoJS.enc.Utf8.parse(process.env.REACT_APP_SECRET_KEY);

        var encryptedPassword = CryptoJS.AES.encrypt(password, key, {mode: CryptoJS.mode.ECB});
        encryptedPassword = encryptedPassword.toString();
        console.log('encrypted', encryptedPassword );

        var encryptedEmail = CryptoJS.AES.encrypt(email, key, {mode: CryptoJS.mode.ECB});
        encryptedEmail = encryptedEmail.toString();
        console.log('encrypted', encryptedEmail );

        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: encryptedEmail, password: encryptedPassword }),
        });

        const data = await response.json();
        setStatusCheck(data.status);
        setLoadingCheck(false);
    };

    return (
        <form onSubmit={checkLoginStatus}>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginComponent;
