import './drivers.css'; 
import React, { useEffect, useState } from 'react'; 
import { FaPlus, FaPen, FaTrash } from "react-icons/fa";
import { useNavigate } from "react-router-dom";


function Results() { 
  const [results, setResults] = useState([]); 
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(''); 
  const [selectedDriver, setSelectedDriver] = useState("");
  const navigate = useNavigate();

  useEffect(() => { 
    fetch('http://127.0.0.1:5000/results')
      .then(response => { 
        if (!response.ok) throw new Error('Failed to fetch results'); 
        return response.json(); 
      })
      .then(data => { 
        setResults(data); 
        setLoading(false); 
      }) 
      .catch(err => { 
        setError(err.message); 
        setLoading(false); 
      });
  }, []); 

  // Filter results based on the selected driver
  const filteredResults = selectedDriver
    ? results.filter(r => `${r.firstName} ${r.lastName}` === selectedDriver)
    : results;

  // Compute statistics for the selected driver
  let driverStats = null;
  if (selectedDriver && filteredResults.length > 0) {
    const validPlacements = filteredResults.filter(r => r.placement !== -1);
    const avgPoints = (filteredResults.reduce((sum, r) => sum + r.points, 0) / filteredResults.length).toFixed(2);
    const avgPlacement = validPlacements.length > 0 
      ? (validPlacements.reduce((sum, r) => sum + r.placement, 0) / validPlacements.length).toFixed(2)
      : "N/A";
    const teamCount = new Set(filteredResults.map(r => r.teamName)).size;

    driverStats = { avgPoints, avgPlacement, teamCount };
  }

  const handleAdd = () => navigate("/add-result");


  return (
    <div className="Drivers">
      <header className="header"> 
        <h1>Results</h1> 
        <button onClick={() => handleAdd()} className="add-driver-icon">
          <FaPlus />
        </button>
      </header>

      {/* Dropdown Filter */}
      <div className="filter-container">
        <label htmlFor="driverFilter">Filter by Driver:</label>
        <select
          id="driverFilter"
          value={selectedDriver}
          onChange={(e) => setSelectedDriver(e.target.value)}
        >
          <option value="">All Drivers</option>
          {[...new Set(results.map(r => `${r.firstName} ${r.lastName}`))].map((name, index) => (
            <option key={index} value={name}>{name}</option>
          ))}
        </select>
      </div>

      {/* Driver stats report */}
      {driverStats && (
        <div className="driver-stats">
          <h3>Stats for {selectedDriver}</h3>
          <p><strong>Average Points per Race:</strong> {driverStats.avgPoints}</p>
          <p><strong>Average Placement:</strong> {driverStats.avgPlacement}</p>
          <p><strong>Teams Raced For:</strong> {driverStats.teamCount}</p>
        </div>
      )}

      {loading && <p className="status-text">Loading results...</p>} 
      {error && <p className="status-text error">Error: {error}</p>} 
      
      {!loading && !error && filteredResults.length > 0 && (
        <div className="table-container">
          <table className="f1-table"> 
            <thead> 
              <tr> 
                <th>Driver</th>
                <th>Constructor</th>
                <th>Grand Prix</th>
                <th>Circuit</th>
                <th>Placement</th>
                <th>Points</th>
                <th>Actions</th>
              </tr> 
            </thead> 
            <tbody> 
              {filteredResults.map((result) => (
                <tr key={result.resultID}>
                  <td> 
                    <span className="driver-name">{result.firstName} <strong>{result.lastName}</strong></span> 
                  </td>
                  <td>
                    <span className="driver-name">
                      <div className="circle" style={{ backgroundColor: result.teamColor }} />
                      {result.teamName}
                    </span> 
                  </td> 
                  <td>{result.grandPrix}</td> 
                  <td>{result.circuitName}</td> 
                  <td>{result.placement === -1 ? "DNF" : result.placement}</td>
                  <td>{result.points}</td>
                  <td>
                    <button className="edit-driver-icon"><FaPen /></button>
                    <button className="delete-driver-icon"><FaTrash /></button>
                  </td>
                </tr>
              ))} 
            </tbody>
          </table>
        </div>
      )}

      {!loading && !error && filteredResults.length === 0 && (
        <p className="status-text">No results found.</p>
      )}
    </div>
  );
}

export default Results;
