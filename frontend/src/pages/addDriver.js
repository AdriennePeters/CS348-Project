import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function AddDriver() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [nation, setNation] = useState("");
  const [debutSeason, setDebutSeason] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();


  const handleSubmit = async (e) => {
    e.preventDefault();

    const driverData = { firstName, lastName, dateOfBirth, nation, debutSeason };

    try {
      const response = await fetch("http://127.0.0.1:5000/addDriver", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(driverData),
      });

      if (!response.ok) throw new Error("Failed to add driver");

      navigate("/drivers");
    } catch (err) {
      setMessage(`Error: ${err.message}`);
    }
  };

  return (
    <div className="add-driver-page">
      <h2>Add New Driver</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
        />
        <input
          type="date"
          placeholder="Date of Birth"
          value={dateOfBirth}
          onChange={(e) => setDateOfBirth(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Nation"
          value={nation}
          onChange={(e) => setNation(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Debut Season"
          value={debutSeason}
          onChange={(e) => setDebutSeason(e.target.value)}
          required
        />
        <button type="submit">Add Driver</button>
      </form>
    </div>
  );
}

export default AddDriver;
