import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import './App.css';

import Homepage from "./components/Homepage"
import Login from "./components/Login"
import Post from "./components/Post"
import UserProfile from "./components/UserProfile";

const App = () => {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Homepage/>}/>
          <Route exact path="/login" element={<Login/>}/>
          <Route exact path="/post" element={<Post/>}/>
          <Route exact path="/profile" element={<UserProfile/>}/>
        </Routes>
    </Router>
  );
}

export default App;
