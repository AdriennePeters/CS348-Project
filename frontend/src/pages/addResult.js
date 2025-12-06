import './drivers.css'; 
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function AddResult() {
  const navigate = useNavigate();

  const [drivers, setDrivers] = useState([]);
  const [constructors, setConstructors] = useState([]);
  const [circuits, setCircuits] = useState([]);

  const [newResult, setNewResult] = useState({
    driverID: "",
    constructorID: "",
    circuitID: "",
    placement: "",
    points: "",
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch all dropdown data (drivers, constructors, circuits)
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [driversRes, constructorsRes, circuitsRes] = await Promise.all([
          fetch("http://127.0.0.1:5000/drivers"),
          fetch("http://127.0.0.1:5000/constructors"),
          fetch("http://127.0.0.1:5000/circuits"),
        ]);

        if (!driversRes.ok || !constructorsRes.ok || !circuitsRes.ok) {
          throw new Error("Failed to fetch data for dropdowns");
        }

        const [driversData, constructorsData, circuitsData] = await Promise.all([
          driversRes.json(),
          constructorsRes.json(),
          circuitsRes.json(),
        ]);

        setDrivers(driversData);
        setConstructors(constructorsData);
        setCircuits(circuitsData);
        setLoading(false);
      } catch (err) {
        console.error(err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Handle form field changes
  const handleChange = (e) => {
    setNewResult({ ...newResult, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Convert placement and points to integers
    const payload = {
      ...newResult,
      placement: parseInt(newResult.placement),
      points: parseFloat(newResult.points),
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/addResult", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) throw new Error("Failed to add result");
      alert("Result successfully added!");
      navigate("/results");
    } catch (err) {
      console.error(err);
      alert("Error adding result. Please try again.");
    }
  };

  if (loading) return <p>Loading form...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="AddResult">
      <h2>Add New Result</h2>
      <form onSubmit={handleSubmit} className="result-form">
        <label>
          Driver:
          <select
            name="driverID"
            value={newResult.driverID}
            onChange={handleChange}
            required
          >
            <option value="">Select Driver</option>
            {drivers.map((driver) => (
              <option key={driver.driverID} value={driver.driverID}>
                {driver.firstName} {driver.lastName}
              </option>
            ))}
          </select>
        </label>

        <label>
          Constructor:
          <select
            name="constructorID"
            value={newResult.constructorID}
            onChange={handleChange}
            required
          >
            <option value="">Select Constructor</option>
            {constructors.map((constructor) => (
              <option key={constructor.constructorID} value={constructor.constructorID}>
                {constructor.teamName}
              </option>
            ))}
          </select>
        </label>

        <label>
          Circuit:
          <select
            name="circuitID"
            value={newResult.circuitID}
            onChange={handleChange}
            required
          >
            <option value="">Select Circuit</option>
            {circuits.map((circuit) => (
              <option key={circuit.circuitID} value={circuit.circuitID}>
                {circuit.circuitName}
              </option>
            ))}
          </select>
        </label>

        <label>
          Placement (use -1 for DNF):
          <input
            type="number"
            name="placement"
            value={newResult.placement}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Points:
          <input
            type="number"
            name="points"
            step="0.5"
            value={newResult.points}
            onChange={handleChange}
            required
          />
        </label>

        <button type="submit">Add Result</button>
        <button type="button" onClick={() => navigate("/results")} className="cancel-btn">
          Cancel
        </button>
      </form>
    </div>
  );
}

export default AddResult;
