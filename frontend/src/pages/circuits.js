import './drivers.css'; 
import React, { useEffect, useState } from 'react'; 
import { countryEmojis } from '../utils/flags';
import { useNavigate } from "react-router-dom";
import { FaPlus, FaPen, FaTrash } from "react-icons/fa";


function Circuits() { 
    const navigate = useNavigate();

    const handleEdit = (circuit) => {
    };

    const handleAdd = () => {
    };

    const handleDelete = async (circuitID) => {
        
    };

    const [circuits, setCircuits] = useState([]); 
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(''); 
    useEffect(() => { 
        fetch('http://127.0.0.1:5000/circuits')
        .then(response => { 
            if (!response.ok) throw new Error('Failed to fetch circuits'); 
            return response.json(); 
        })
        .then(data => { 
            setCircuits(data); 
            setLoading(false); 
        }) 
        .catch(err => { 
            setError(err.message); 
            setLoading(false); 
        });
     }, []); 
     
     return (
         <div className="Drivers">
             <header className="header"> 
                <h1>Circuits</h1> 
                <button onClick={() => handleAdd()} className="add-driver-icon">
                    <FaPlus />
                </button>
             </header> 
             
             {loading && <p className="status-text">Loading circuits...</p>} 
             {error && <p className="status-text error">Error: {error}</p>} 
             
             {!loading && !error && ( 
                <div className="table-container">
                <table className="f1-table"> 
                <thead> 
                    <tr> 
                        <th>Circuit Name</th>
                        <th>Country</th>
                        <th>Grand Prix</th>
                        <th>Turns</th>
                        <th>Length</th>
                        <th>Actions</th>
                    </tr> 
                </thead> 
                <tbody> 
                    {circuits.map((circuit, index) => (
                         <tr key={circuit.circuitID}>
                             <td> 
                                <span className="driver-name"> {circuit.circuitName}</span> 
                            </td>
                            <td>
                                <span className="nation-cell">
                                    {circuit.circuitCountry}{" "}{countryEmojis[circuit.circuitCountry] || "🏳️"}
                                </span>
                            </td> 
                            <td>{circuit.circuitGrandPrix}</td> 
                            <td>{circuit.circuitTurns}</td>
                            <td>{circuit.circuitLength} km</td>
                            <td>
                                <button onClick={() => handleEdit(circuit)} className="edit-driver-icon">
                                    <FaPen />
                                </button>
                                <button onClick={() => handleDelete(circuit.circuitID)} className="delete-driver-icon">
                                    <FaTrash />
                                </button>
                            </td>
                        </tr> )
                    )} 
                </tbody> </table> </div> )} 
                
                {!loading && !error && circuits.length === 0 && ( 
                    <p className="status-text">No circuits found.</p> 
                )} 
                </div> 
                ); 
            } 
        export default Circuits;