import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function EditDriver() {
  const { state } = useLocation(); // may be null if page refreshed
  const { driverId } = useParams();
  const navigate = useNavigate();

  const [driver, setDriver] = useState({
    firstName: "",
    lastName: "",
    dateOfBirth: "",
    nation: "",
    debutSeason: "",
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (state?.driver) {
      // If driver passed via navigate, use it
      setDriver(state.driver);
      setLoading(false);
    } else {
      // Otherwise fetch from backend
      fetch(`http://127.0.0.1:5000/getDriver/${driverId}`)
        .then((res) => res.json())
        .then((data) => {
          setDriver({
            firstName: data.firstName || data.first_name,
            lastName: data.lastName || data.last_name,
            dateOfBirth: data.dateOfBirth || data.date_of_birth,
            nation: data.nation,
            debutSeason: data.debutSeason || data.debut_season,
          });
          setLoading(false);
        })
        .catch((err) => {
          console.error("Error fetching driver:", err);
          setLoading(false);
        });
    }
  }, [state, driverId]);

  const handleChange = (e) => {
    setDriver({ ...driver, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch(`http://127.0.0.1:5000/editDriver/${driverId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(driver),
    });
    navigate("/drivers");
  };

  return (
    <div className="EditDriver">
      <h2>Edit Driver</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="firstName"
          value={driver.firstName}
          onChange={handleChange}
          placeholder="First Name"
        />
        <input
          name="lastName"
          value={driver.lastName}
          onChange={handleChange}
          placeholder="Last Name"
        />
        <input
          name="dateOfBirth"
          value={driver.dateOfBirth}
          onChange={handleChange}
          placeholder="YYYY-MM-DD"
        />
        <input
          name="nation"
          value={driver.nation}
          onChange={handleChange}
          placeholder="Nation"
        />
        <input
          name="debutSeason"
          value={driver.debutSeason}
          onChange={handleChange}
          placeholder="Debut Season"
        />
        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
}

export default EditDriver;