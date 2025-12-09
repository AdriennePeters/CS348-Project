import './drivers.css'; 
import React, { useEffect, useState } from 'react'; 
import { countryEmojis } from '../utils/flags';
import { useNavigate } from "react-router-dom";
import { FaPlus, FaPen, FaTrash, FaTimes } from "react-icons/fa";


function Drivers() { 
    const navigate = useNavigate();

    const handleEdit = (driver) => {
        navigate(`/edit-driver/${driver.driverID}`, { state: { driver } });
    };

    const handleAdd = () => {
        navigate("/add-driver");
    };

    const handleRemoveFilter = () => {
        setSelectedDriver("");
    };

    const handleDelete = async (driverID) => {
        const confirmed = window.confirm(
            "Are you sure you want to delete this driver?"
        );
        if (!confirmed) return;
        
        try {
            const response = await fetch(`http://127.0.0.1:5000/deleteDriver/${driverID}`, {
            method: "DELETE",
            });
        
            if (!response.ok) throw new Error("Failed to delete driver");
        
            // Remove the deleted driver from state so UI updates
            setDrivers(drivers.filter((driver) => driver.driverID !== driverID));
        } catch (err) {
            console.error(err);
            alert("Error deleting driver. Please try again.");
        }
    };

    const [drivers, setDrivers] = useState([]); 
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(''); 
    const [selectedDriver, setSelectedDriver] = useState("");

    useEffect(() => { 
        const fetchDrivers = () => {
            fetch('http://127.0.0.1:5000/drivers')
            .then(response => { 
                if (!response.ok) throw new Error('Failed to fetch drivers'); 
                return response.json(); 
            })
            .then(data => { 
                setDrivers(data); 
                setLoading(false); 
            }) 
            .catch(err => { 
                setError(err.message); 
                setLoading(false); 
            });
        }
        fetchDrivers();

        // Set up interval to fetch every 5 seconds
        const interval = setInterval(fetchDrivers, 5000);

        // Cleanup interval on unmount
        return () => clearInterval(interval);
     }, []); 

     // Filter results based on the selected driver
    const filteredDrivers = selectedDriver
    ? drivers.filter(r => `${r.firstName} ${r.lastName}` === selectedDriver)
    : drivers;
     
     return (
         <div className="Drivers">
             <header className="header"> 
                <h1>Drivers</h1> 
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
                {[...new Set(drivers.map(r => `${r.firstName} ${r.lastName}`))].map((name, index) => (
                    <option key={index} value={name}>{name}</option>
                ))}
                </select>

                <div className="remove-filter">
                <button onClick={() => handleRemoveFilter()} className="add-driver-icon">
                    <FaTimes />
                </button>
            </div>
            </div>

            
             
             {loading && <p className="status-text">Loading drivers...</p>} 
             {error && <p className="status-text error">Error: {error}</p>} 
             
             {!loading && !error && filteredDrivers.length > 0 &&( 
                <div className="table-container">
                <table className="f1-table"> 
                <thead> 
                    <tr> 
                        <th>Driver</th>
                        <th>Date of Birth</th>
                        <th>Nation</th>
                        <th>Debut Season</th>
                        <th>Actions</th>
                    </tr> 
                </thead> 
                <tbody> 
                    {filteredDrivers.map((driver, index) => (
                         <tr key={driver.driverID}>
                             <td> 
                                <span className="driver-name"> {driver.firstName} <strong>{driver.lastName}</strong> </span> 
                            </td>
                                <td>{driver.dateOfBirth}</td> 
                                <td>
                                    <span className="nation-cell">
                                        {driver.nation}{" "}{countryEmojis[driver.nation] || "🏳️"}
                                    </span>
                                </td> 
                                <td>{driver.debutSeason}</td> 
                                <td>
                                <button onClick={() => handleEdit(driver)} className="edit-driver-icon">
                                    <FaPen />
                                </button>
                                <button onClick={() => handleDelete(driver.driverID)} className="delete-driver-icon">
                                    <FaTrash />
                                </button>
                                </td>
                        </tr> )
                    )} 
                </tbody> </table> </div> )} 
                
                {!loading && !error && drivers.length === 0 && ( 
                    <p className="status-text">No drivers found.</p> 
                )} 
                </div> 
                ); 
            } 
        export default Drivers;