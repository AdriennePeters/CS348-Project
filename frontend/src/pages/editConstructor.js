import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function EditConstructor() {
    const { state } = useLocation(); 
    const { constructorId } = useParams();
    const navigate = useNavigate();

    const [constructor, setConstructor] = useState({
        teamName: "",
        teamColor: "",
        foundedYear: "",
        countryBase: ""
    });

    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (state?.constructor) {
          // If constructor passed via navigate, use it
          setConstructor(state.constructor);
          setLoading(false);
        } else {
          // Otherwise fetch from backend
          fetch(`http://127.0.0.1:5000/getConstructor/${constructorId}`)
            .then((res) => res.json())
            .then((data) => {
              setConstructor({
                teamName: data.teamName,
                teamColor: data.teamColor,
                foundedYear: data.foundedYear,
                countryBase: data.countryBase
              });
              setLoading(false);
            })
            .catch((err) => {
              console.error("Error fetching Constructor:", err);
              setLoading(false);
            });
        }
      }, [state, constructorId]);

      const handleChange = (e) => {
        setConstructor({ ...constructor, [e.target.name]: e.target.value });
      };

      const handleSubmit = async (e) => {
        e.preventDefault();
        await fetch(`http://127.0.0.1:5000/editConstructor/${constructorId}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(constructor),
        });
        navigate("/constructors");
      };

      return (
        <div className="EditConstructor">
          <h2>Edit Constructor</h2>
          <form onSubmit={handleSubmit}>
            <input
              name="teamName"
              value={constructor.teamName}
              onChange={handleChange}
              placeholder="Constructor Name"
            />
            <input
              type = "color"
              name="teamColor"
              value={constructor.teamColor || "#000000"}
              onChange={handleChange}
              placeholder="Team Color"
            />
            <input
              name="foundedYear"
              value={constructor.foundedYear}
              onChange={handleChange}
              placeholder="YYYY"
            />
            <input
              name="countryBase"
              value={constructor.countryBase}
              onChange={handleChange}
              placeholder="Country Base"
            />
            <button type="submit">Save Changes</button>
          </form>
        </div>
      );
}
export default EditConstructor;