import './constructors.css'; 
import React, { useEffect, useState } from 'react'; 
import { countryEmojis } from '../utils/flags';
import { useNavigate } from "react-router-dom";
import { FaPlus, FaPen, FaTrash } from "react-icons/fa";


function Constructors() { 
     
    const [constructors, setConsturctors] = useState([]);
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(''); 
    const navigate = useNavigate();


    useEffect(() => {
        fetch('http://127.0.0.1:5000/constructors').then(
            response => {
                if(!response.ok) throw new Error('Failed to fetch constructors');
                return response.json();
            }
        ).then(
            data=> {
                setConsturctors(data);
                setLoading(false);
            }
        ).catch(err => {
            setError(err.message);
            setLoading(false);
        });
    }, []);


    const handleEdit = (constructor) => {
        navigate(`/edit-constructor/${constructor.constructorID}`, { state: { constructor } });
    };

    const handleDelete = async (constructorID) => {
        
    };

    const handleAdd = () => {

    };

     return (
            <div className="Constructors">
                <header className="header">
                    <h1>Constructors</h1>

                    <button onClick={() => handleAdd()} className="add-constructor-icon">
                        <FaPlus />
                    </button>
                </header>

                {loading && <p className="status-text">Loading constructors...</p>} 
                {error && <p className="status-text error">Error: {error}</p>} 

                {
                    !loading && !error && (
                        <div className="table-container">
                            <table className="f1-table">
                                <thead>
                                    <tr>
                                        <th>Constructor</th>
                                        <th>Founded</th>
                                        <th>Country Based</th>
                                        <th>Actions</th>
                                    </tr>
                                </thead>

                                <tbody>
                                    {constructors.map((constructor, index) => (
                                        <tr key={constructor.constructorID}>
                                            <td>
                                                <div className="circle" style={{ backgroundColor: constructor.teamColor }} />{constructor.teamName}
                                            </td>

                                            <td>{constructor.foundedYear}</td>

                                            <td>
                                                <span className="nation-cell">
                                                    {constructor.countryBase}{" "}{countryEmojis[constructor.countryBase] || "🏳️"}
                                                </span> 
                                            </td>
                                            <td>
                                                <button onClick={() => handleEdit(constructor)} className="edit-constructor-icon">
                                                    <FaPen />
                                                </button>
                                                
                                                <button onClick={() => handleDelete(constructor.constructorID)} className="delete-constructor-icon">
                                                    <FaTrash />
                                                </button>
                                            </td>
                                        </tr>
                                        
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    )
                }
            </div>
        ); 
    } 
    export default Constructors;