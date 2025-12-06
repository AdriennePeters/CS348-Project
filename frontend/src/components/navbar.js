import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css";
import logo from "../F1-logo.png"

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo"><img src={logo} alt="Logo" style={{ width: "110px", height: "110px", objectFit: "contain" }} /></div>
      <ul className="nav-links">
        <li><Link to="/drivers">Drivers</Link></li>
        <li><Link to="/constructors">Constructors</Link></li>
        <li><Link to="/circuits">Circuits</Link></li>
        <li><Link to="/results">Results</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
