import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Admin from './Admin';
import History from './History';

import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <BrowserRouter>
        <Routes>
            <Route exact path="/" element={<App />}>
                <Route path="admin" element={<Admin />} />
                <Route path="history" element={<History />} />
            </Route>
        </Routes>
    </BrowserRouter>
);