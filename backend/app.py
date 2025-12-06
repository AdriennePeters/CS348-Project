from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#======================
# Drivers
#======================
class Circuits(db.Model):
    circuitID = db.Column(db.Integer, primary_key=True)
    circuitName = db.Column(db.String(150))
    circuitLength = db.Column(db.Double)
    circuitTurns = db.Column(db.Integer)
    circuitGrandPrix = db.Column(db.String(150))
    circuitCountry = db.Column(db.String(150))
    circuitCity = db.Column(db.String(150))

    def to_json(self):
        return {
            "circuitID": self.circuitID,
            "circuitName": self.circuitName,
            "circuitLength": self.circuitLength,
            "circuitTurns": self.circuitTurns,
            "circuitGrandPrix": self.circuitGrandPrix,
            "circuitCountry": self.circuitCountry,
            "circuitCity": self.circuitCity
        }

#======================
# Constructors
#======================
class Constructors(db.Model):
    constructorID = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(100), nullable=False)
    teamColor = db.Column(db.String(50))
    foundedYear = db.Column(db.Integer)
    countryBase = db.Column(db.String(100))

    def to_json(self):
        return {
            "constructorID": self.constructorID,
            "teamName": self.teamName,
            "teamColor": self.teamColor,
            "foundedYear": self.foundedYear,
            "countryBase": self.countryBase,
        }

#======================
# Drivers
#======================
class Drivers(db.Model):
    driverID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    dateOfBirth = db.Column(db.String(20))
    nation = db.Column(db.String(100))
    debutSeason = db.Column(db.Integer)

    def to_json(self):
        return{
            "driverID": self.driverID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "dateOfBirth": self.dateOfBirth,
            "nation": self.nation,
            "debutSeason": self.debutSeason,
        }

#======================
# Results
#======================
class Results(db.Model):
    resultID = db.Column(db.Integer, primary_key=True)
    driverID = db.Column(db.Integer, db.ForeignKey('drivers.driverID'), nullable=False)
    constructorID = db.Column(db.Integer, db.ForeignKey('constructors.constructorID'), nullable=False)
    circuitID =db.Column(db.Integer, db.ForeignKey('circuits.circuitID'), nullable=False)
    placement = db.Column(db.Integer) #-1 indicates DNF
    points = db.Column(db.Integer)

    def to_json(self):
        return{
            "resultID": self.resultID,
            "driverID": self.driverID,
            "constructorID": self.constructorID,
            "circuitID": self.circuitID,
            "placement": self.placement,
            "points": self.points
        }

#======================
# App Routes
#======================
@app.route('/')
def home():
    return jsonify({"message": "Flask API is running, sent from backend"})

@app.route('/constructors', methods=['GET'])
def get_constructors():
    constructors = Constructors.query.all()
    return jsonify([c.to_json() for c in constructors])

@app.route("/getConstructor/<int:constructor_id>", methods=["GET"])
def get_constructor(constructor_id):
    constructor = Constructors.query.get(constructor_id)
    db.session.commit()
    if not constructor:
        return jsonify({"error": "Constructor not found"}), 404
    return jsonify(constructor.to_json())

@app.route("/editConstructor/<int:constructor_id>", methods=["PUT"])
def edit_constructor(constructor_id):
    data = request.get_json()

    constructor = Constructors.query.get(constructor_id)

    # Update fields if they exist in the request
    constructor.teamName = data.get("teamName", constructor.teamName)
    constructor.teamColor = data.get("teamColor", constructor.teamColor)
    constructor.foundedYear = data.get("foundedYear", constructor.foundedYear)
    constructor.countryBase = data.get("countryBase", constructor.countryBase)

    db.session.commit()
    return jsonify({"message": "Constructor updated successfully", "constructor": constructor.to_json()})

@app.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = Drivers.query.all()
    return jsonify([d.to_json() for d in drivers])

@app.route('/addDriver', methods=['POST'])
def add_driver():
    data = request.get_json()
    print(data)
    try:
        new_driver = Drivers(
            firstName=data["firstName"],
            lastName=data["lastName"],
            dateOfBirth=data["dateOfBirth"],
            nation=data["nation"],
            debutSeason=int(data["debutSeason"])
        )

        db.session.add(new_driver)
        db.session.commit()

        return jsonify({"message": "Driver added successfully!", "driverID": new_driver.driverID}), 201

    except KeyError as e:
        return jsonify({"error": "Missing field: {e}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add driver", "details": str(e)}), 500

@app.route("/editDriver/<int:driver_id>", methods=["PUT"])
def edit_driver(driver_id):
    data = request.get_json()

    driver = Drivers.query.get(driver_id)

    # Update fields if they exist in the request
    driver.firstName = data.get("firstName", driver.firstName)
    driver.lastName = data.get("lastName", driver.lastName)
    driver.dateOfBirth = data.get("dateOfBirth", driver.dateOfBirth)
    driver.nation = data.get("nation", driver.nation)
    driver.debutSeason = data.get("debutSeason", driver.debutSeason)

    db.session.commit()
    return jsonify({"message": "Driver updated successfully", "driver": driver.to_json()})

@app.route("/getDriver/<int:driver_id>", methods=["GET"])
def get_driver(driver_id):
    driver = Drivers.query.get(driver_id)
    db.session.commit()
    if not driver:
        return jsonify({"error": "Driver not found"}), 404
    return jsonify(driver.to_json())

@app.route("/deleteDriver/<int:driver_id>", methods=["DELETE"])
def delete_driver(driver_id):
    driver = Drivers.query.get(driver_id)  # Fetch the driver by ID
    db.session.delete(driver)  # Mark for deletion
    db.session.commit() 
    return jsonify({"message": "deleted"}), 200

@app.route('/circuits', methods=['GET'])
def get_circuits():
    circuits = Circuits.query.all()
    return jsonify([c.to_json() for c in circuits])

@app.route('/results', methods=['GET'])
def get_results():
    results = (
        db.session.query(
            Results.resultID,
            Results.driverID,
            Drivers.firstName,
            Drivers.lastName,
            Results.constructorID,
            Constructors.teamName,
            Constructors.teamColor,
            Results.circuitID,
            Circuits.circuitName,
            Circuits.circuitGrandPrix,
            Circuits.circuitCity,
            Circuits.circuitCountry,
            Results.placement,
            Results.points
        )
        .join(Drivers, Results.driverID == Drivers.driverID)
        .join(Constructors, Results.constructorID == Constructors.constructorID)
        .join(Circuits, Results.circuitID == Circuits.circuitID)
        .all()
    )

    results_list = [
        {
            "resultID": r.resultID,
            "driverID": r.driverID,
            "firstName": r.firstName,
            "lastName": r.lastName,
            "constructorID": r.constructorID,
            "teamName": r.teamName,
            "teamColor": r.teamColor,
            "circuitID": r.circuitID,
            "circuitName": r.circuitName,
            "grandPrix": r.circuitGrandPrix,
            "city": r.circuitCity,
            "country": r.circuitCountry,
            "placement": r.placement,
            "points": r.points
        }
        for r in results
    ]
    return jsonify(results_list)

@app.route('/addResult', methods=['POST'])
def add_result():
    data = request.get_json()
    driver_id = data.get('driverID')
    constructor_id = data.get('constructorID')
    circuit_id = data.get('circuitID')
    placement = data.get('placement')
    points = data.get('points')
    
    new_result = Results(driverID = driver_id, constructorID = constructor_id, circuitID =circuit_id, placement = placement, points = points)

    db.session.add(new_result)
    db.session.commit()
    return jsonify({"message": "result added"})
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)