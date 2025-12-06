import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from './components/navbar';

import Drivers from "./pages/drivers";
import AddDriver from "./pages/addDriver";
import EditDriver from "./pages/editDriver";
import Constructors from './pages/constructors';
import EditConstructor from './pages/editConstructor';
import Circuits from './pages/circuits';
import Results from './pages/results';
import AddResult from './pages/addResult';

function App() {
  return (
      <Router>
      <Navbar/>
      <div style={{ padding: "2rem" }}>
        <Routes>
          <Route path="/drivers" element={<Drivers />} />
          <Route path="/add-driver" element={<AddDriver />} />
          <Route path="/edit-driver/:driverId" element={<EditDriver />} />
          <Route path="/constructors" element={<Constructors />} />
          <Route path="/edit-constructor/:constructorId" element={<EditConstructor />} />
          <Route path="/circuits" element={<Circuits />} />
          <Route path="/results" element={<Results />} />
          <Route path="/add-result" element={<AddResult />} />
        </Routes>
      </div>
      </Router>
    
  );
}

export default App;
