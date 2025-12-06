from app import app, db, Constructors, Drivers, Circuits, Results
drivers_data = [
    {"firstName": "Max",       "lastName": "Verstappen",     "dateOfBirth": "1997-09-30", "nation": "Netherlands",     "debutSeason": 2015},
    {"firstName": "Yuki",      "lastName": "Tsunoda",        "dateOfBirth": "2000-05-11", "nation": "Japan",           "debutSeason": 2021},
    {"firstName": "Lewis",     "lastName": "Hamilton",       "dateOfBirth": "1985-01-07", "nation": "Great Britain",   "debutSeason": 2007},
    {"firstName": "Charles",   "lastName": "Leclerc",        "dateOfBirth": "1997-10-16", "nation": "Monaco",          "debutSeason": 2018},
    {"firstName": "George",    "lastName": "Russell",        "dateOfBirth": "1998-02-15", "nation": "Great Britain",   "debutSeason": 2019},
    {"firstName": "Kimi", "lastName": "Antonelli",     "dateOfBirth": "2006-08-25", "nation": "Italy",           "debutSeason": 2025},
    {"firstName": "Lando",     "lastName": "Norris",         "dateOfBirth": "1999-11-13", "nation": "Great Britain",   "debutSeason": 2019},
    {"firstName": "Oscar",     "lastName": "Piastri",        "dateOfBirth": "2001-04-06", "nation": "Australia",       "debutSeason": 2023},
    {"firstName": "Fernando",  "lastName": "Alonso",         "dateOfBirth": "1981-07-29", "nation": "Spain",           "debutSeason": 2001},
    {"firstName": "Lance",     "lastName": "Stroll",         "dateOfBirth": "1998-10-29", "nation": "Canada",          "debutSeason": 2017},
    {"firstName": "Pierre",    "lastName": "Gasly",          "dateOfBirth": "1996-02-07", "nation": "France",          "debutSeason": 2017},
    {"firstName": "Jack",      "lastName": "Doohan",         "dateOfBirth": "2003-01-18", "nation": "Australia",       "debutSeason": 2025},
    {"firstName": "Alex",      "lastName": "Albon",          "dateOfBirth": "1996-03-23", "nation": "Thailand",        "debutSeason": 2019},
    {"firstName": "Carlos",    "lastName": "Sainz",          "dateOfBirth": "1994-09-01", "nation": "Spain",           "debutSeason": 2015},
    {"firstName": "Nico",      "lastName": "Hulkenberg",     "dateOfBirth": "1987-08-19", "nation": "Germany",         "debutSeason": 2010},
    {"firstName": "Gabriel",   "lastName": "Bortoleto",      "dateOfBirth": "2004-10-14", "nation": "Brazil",          "debutSeason": 2025},
    {"firstName": "Oliver",    "lastName": "Bearman",        "dateOfBirth": "2005-01-29", "nation": "United Kingdom",  "debutSeason": 2025},
    {"firstName": "Esteban",   "lastName": "Ocon",           "dateOfBirth": "1996-09-17", "nation": "France",          "debutSeason": 2016},
    {"firstName": "Franco",    "lastName": "Colapinto",      "dateOfBirth": "2004-10-17", "nation": "Argentina",       "debutSeason": 2025},
    {"firstName": "Isack",     "lastName": "Hadjar",         "dateOfBirth": "2004-09-28", "nation": "France",          "debutSeason": 2025},
    {"firstName": "Liam",      "lastName": "Lawson",         "dateOfBirth": "2002-02-11", "nation": "New Zealand",     "debutSeason": 2023},
    {"firstName": "Sergio", "lastName": "Perez", "dateOfBirth": "1990-01-26", "nation": "Mexico", "debutSeason": 2011},
    {"firstName": "Valtteri", "lastName": "Bottas", "dateOfBirth": "1989-08-28", "nation": "Finland", "debutSeason": 2013},
    {"firstName": "Logan", "lastName": "Sargeant", "dateOfBirth": "2000-12-31", "nation": "USA", "debutSeason": 2023},

    # Notable Past Drivers
    {"firstName": "Michael", "lastName": "Schumacher", "dateOfBirth": "1969-01-03", "nation": "Germany", "debutSeason": 1991},
    {"firstName": "Ayrton", "lastName": "Senna", "dateOfBirth": "1960-03-21", "nation": "Brazil", "debutSeason": 1984},
    {"firstName": "Alain", "lastName": "Prost", "dateOfBirth": "1955-02-24", "nation": "France", "debutSeason": 1980},
    {"firstName": "Niki", "lastName": "Lauda", "dateOfBirth": "1949-02-22", "nation": "Austria", "debutSeason": 1971}
]

teams_data = [
    # Current Teams
    {"teamName": "Red Bull Racing", "baseCountry": "United Kingdom", "foundedYear": 2005, "active": True, "teamColor": "#1E41FF"},
    {"teamName": "Mercedes AMG Petronas F1 Team", "baseCountry": "United Kingdom", "foundedYear": 2010, "active": True, "teamColor": "#00D2BE"},
    {"teamName": "Scuderia Ferrari", "baseCountry": "Italy", "foundedYear": 1929, "active": True, "teamColor": "#DC0000"},
    {"teamName": "McLaren F1 Team", "baseCountry": "United Kingdom", "foundedYear": 1963, "active": True, "teamColor": "#FF8700"},
    {"teamName": "Aston Martin Aramco Cognizant F1 Team", "baseCountry": "United Kingdom", "foundedYear": 2021, "active": True, "teamColor": "#006F62"},
    {"teamName": "BWT Alpine F1 Team", "baseCountry": "France", "foundedYear": 2021, "active": True, "teamColor": "#0090FF"},
    {"teamName": "Williams Racing", "baseCountry": "United Kingdom", "foundedYear": 1977, "active": True, "teamColor": "#005AFF"},
    {"teamName": "Stake F1 Team Kick Sauber", "baseCountry": "Switzerland", "foundedYear": 1993, "active": True, "teamColor": "#00F01C"},
    {"teamName": "Visa Cash App RB Formula One Team", "baseCountry": "nited Kingdom", "foundedYear": 2006, "active": True, "teamColor": "#9EB6FF"},
    {"teamName": "Haas F1 Team", "baseCountry": "United States", "foundedYear": 2016, "active": True, "teamColor": "#B0B0B0"},

    # Notable Past Teams
    {"teamName": "Benetton Formula", "baseCountry": "United Kingdom", "foundedYear": 1986, "active": False, "teamColor": "#008000"},
    {"teamName": "Renault F1 Team", "baseCountry": "France", "foundedYear": 1977, "active": False, "teamColor": "#FFF500"},
    {"teamName": "Lotus F1 Team", "baseCountry": "United Kingdom", "foundedYear": 1981, "active": False, "teamColor": "#000000"},
    {"teamName": "Tyrrell Racing", "baseCountry": "United Kingdom", "foundedYear": 1970, "active": False, "teamColor": "#0000FF"},
    {"teamName": "Brawn GP", "baseCountry": "United Kingdom", "foundedYear": 2009, "active": False, "teamColor": "#FFFFFF"},
    {"teamName": "Brabham", "baseCountry": "United Kingdom", "foundedYear": 1960, "active": False, "teamColor": "#0000FF"},
    {"teamName": "BAR Honda", "baseCountry": "United Kingdom", "foundedYear": 1999, "active": False, "teamColor": "#FF0000"},
    {"teamName": "Jordan Grand Prix", "baseCountry": "Ireland", "foundedYear": 1991, "active": False, "teamColor": "#FFCC00"},
    {"teamName": "Minardi", "baseCountry": "Italy", "foundedYear": 1985, "active": False, "teamColor": "#800080"},
    {"teamName": "Arrows", "baseCountry": "United Kingdom", "foundedYear": 1978, "active": False, "teamColor": "#00FF00"},
    {"teamName": "Manor Marussia F1 Team", "baseCountry": "United Kingdom", "foundedYear": 2010, "active": False, "teamColor": "#FF0000"},
    {"teamName": "Caterham F1 Team", "baseCountry": "United Kingdom", "foundedYear": 2010, "active": False, "teamColor": "#008000"},
    {"teamName": "HRT F1 Team", "baseCountry": "Spain", "foundedYear": 2010, "active": False, "teamColor": "#FF0000"},
    {"teamName": "Super Aguri F1 Team", "baseCountry": "Japan", "foundedYear": 2006, "active": False, "teamColor": "#FFFFFF"},
    {"teamName": "Prost Grand Prix", "baseCountry": "France", "foundedYear": 1997, "active": False, "teamColor": "#0000FF"},
    {"teamName": "Sauber F1 Team", "baseCountry": "Switzerland", "foundedYear": 1993, "active": False, "teamColor": "#0047AB"},
    {"teamName": "BMW Sauber F1 Team", "baseCountry": "Germany", "foundedYear": 2006, "active": False, "teamColor": "#0066CC"},
    {"teamName": "Ligier", "baseCountry": "France", "foundedYear": 1976, "active": False, "teamColor": "#00FFFF"},
    {"teamName": "Shadow Racing Team", "baseCountry": "United Kingdom", "foundedYear": 1973, "active": False, "teamColor": "#FF00FF"},
]

circuit_data = [
    {"circuitName": "Adelaide Street Circuit" , "circuitLength": 3.780, "circuitTurns": 16, "circuitGrandPrix": "Australian Grand Prix", "circuitCountry": "Australia", "circuitCity": "Adelaide" },
    {"circuitName": "Ain-Diab Circuit" , "circuitLength": 7.618, "circuitTurns": 18, "circuitGrandPrix": "Moroccan Grand Prix", "circuitCountry": "Morocco", "circuitCity": "Casablanca" },
    {"circuitName": "Aintree Motor Racing Circuit" , "circuitLength": 4.828, "circuitTurns": 12, "circuitGrandPrix": "British Grand Prix", "circuitCountry": "United Kingdom", "circuitCity": "Aintree" },
    {"circuitName": "Albert Park Circuit" , "circuitLength": 5.278, "circuitTurns": 14, "circuitGrandPrix": "Australian Grand Prix", "circuitCountry": "Australia", "circuitCity": "Melbourne" },
    {"circuitName": "Algarve International Circuit" , "circuitLength": 4.653, "circuitTurns": 15, "circuitGrandPrix": "Portuguese Grand Prix", "circuitCountry": "Portugal", "circuitCity": "Portimão" },
    {"circuitName": "Autódromo do Estoril" , "circuitLength": 4.360, "circuitTurns": 13, "circuitGrandPrix": "Portuguese Grand Prix", "circuitCountry": "Portugal", "circuitCity": "Estoril" },
    {"circuitName": "Autódromo Hermanos Rodríguez" , "circuitLength": 4.304, "circuitTurns": 17, "circuitGrandPrix": "Mexican Grand Prix,Mexico City Grand Prix", "circuitCountry": "Mexico", "circuitCity": "Mexico City" },
    {"circuitName": "Autódromo Internacional do Rio de Janeiro" , "circuitLength": 5.031, "circuitTurns": 11, "circuitGrandPrix": "Brazilian Grand Prix", "circuitCountry": "Brazil", "circuitCity": "Rio de Janeiro" },
    {"circuitName": "Autodromo Internazionale del Mugello" , "circuitLength": 5.245, "circuitTurns": 15, "circuitGrandPrix": "Tuscan Grand Prix", "circuitCountry": "Italy", "circuitCity": "Scarperia e San Piero" },
    {"circuitName": "Autodromo Internazionale Enzo e Dino Ferrari" , "circuitLength": 4.909, "circuitTurns": 19, "circuitGrandPrix": "Italian Grand Prix,San Marino Grand Prix,Emilia Romagna Grand Prix", "circuitCountry": "Italy", "circuitCity": "Imola" },
    {"circuitName": "Autodromo José Carlos Pace" , "circuitLength": 4.309, "circuitTurns": 15, "circuitGrandPrix": "Brazilian Grand Prix,São Paulo Grand Prix", "circuitCountry": "Brazil", "circuitCity": "São Paulo" },
    {"circuitName": "Autodromo Nazionale di Monza" , "circuitLength": 5.793, "circuitTurns": 11, "circuitGrandPrix": "Italian Grand Prix", "circuitCountry": "Italy", "circuitCity": "Monza" },
    {"circuitName": "Autódromo Oscar y Juan Gálvez" , "circuitLength": 4.259, "circuitTurns": 18, "circuitGrandPrix": "Argentine Grand Prix", "circuitCountry": "Argentina", "circuitCity": "Buenos Aires" },
    {"circuitName": "AVUS" , "circuitLength": 8.300, "circuitTurns": 4, "circuitGrandPrix": "German Grand Prix", "circuitCountry": "Germany", "circuitCity": "Berlin" },
    {"circuitName": "Bahrain International Circuit" , "circuitLength": 5.412, "circuitTurns": 15, "circuitGrandPrix": "Bahrain Grand Prix,Sakhir Grand Prix", "circuitCountry": "Bahrain", "circuitCity": "Sakhir" },
    {"circuitName": "Baku City Circuit" , "circuitLength": 6.003, "circuitTurns": 20, "circuitGrandPrix": "European Grand Prix,Azerbaijan Grand Prix", "circuitCountry": "Azerbaijan", "circuitCity": "Baku" },
    {"circuitName": "Brands Hatch Circuit" , "circuitLength": 4.206, "circuitTurns": 11, "circuitGrandPrix": "British Grand Prix,European Grand Prix", "circuitCountry": "United Kingdom", "circuitCity": "West Kingsdown" },
    {"circuitName": "Buddh International Circuit" , "circuitLength": 5.141, "circuitTurns": 16, "circuitGrandPrix": "Indian Grand Prix", "circuitCountry": "India", "circuitCity": "Greater Noida" },
    {"circuitName": "Bugatti Au Mans" , "circuitLength": 4.430, "circuitTurns": 8, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Le Mans" },
    {"circuitName": "Caesars Palace Grand Prix Circuit" , "circuitLength": 3.650, "circuitTurns": 14, "circuitGrandPrix": "Caesars Palace Grand Prix", "circuitCountry": "United States", "circuitCity": "Paradise" },
    {"circuitName": "Charade Circuit" , "circuitLength": 8.055, "circuitTurns": 38, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Saint-Genès-Champanelle" },
    {"circuitName": "Circuit Bremgarten" , "circuitLength": 7.208, "circuitTurns": 14, "circuitGrandPrix": "Swiss Grand Prix", "circuitCountry": "Switzerland", "circuitCity": "Bern" },
    {"circuitName": "Circuit de Barcelona-Catalunya" , "circuitLength": 4.657, "circuitTurns": 14, "circuitGrandPrix": "Spanish Grand Prix", "circuitCountry": "Spain", "circuitCity": "Montmeló" },
    {"circuitName": "Circuit de Monaco" , "circuitLength": 3.337, "circuitTurns": 19, "circuitGrandPrix": "Monaco Grand Prix", "circuitCountry": "Monaco", "circuitCity": "Monte Carlo" },
    {"circuitName": "Circuit de Nevers Magny-Cours" , "circuitLength": 4.411, "circuitTurns": 16, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Magny-Cours" },
    {"circuitName": "Circuit de Pedralbes" , "circuitLength": 6.316, "circuitTurns": 6, "circuitGrandPrix": "Spanish Grand Prix", "circuitCountry": "Spain", "circuitCity": "Barcelona" },
    {"circuitName": "Circuit de Reims-Gueux" , "circuitLength": 8.302, "circuitTurns": 6, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Gueux" },
    {"circuitName": "Circuit de Spa-Francorchamps" , "circuitLength": 7.004, "circuitTurns": 20, "circuitGrandPrix": "Belgian Grand Prix", "circuitCountry": "Belgium", "circuitCity": "Stavelot" },
    {"circuitName": "Circuit Dijon-Prenois" , "circuitLength": 3.886, "circuitTurns": 12, "circuitGrandPrix": "French Grand Prix,Swiss Grand Prix", "circuitCountry": "France", "circuitCity": "Prenois" },
    {"circuitName": "Circuit Gilles-Villeneuve" , "circuitLength": 4.361, "circuitTurns": 14, "circuitGrandPrix": "Canadian Grand Prix", "circuitCountry": "Canada", "circuitCity": "Montreal" },
    {"circuitName": "Circuit Mont-Tremblant" , "circuitLength": 4.265, "circuitTurns": 15, "circuitGrandPrix": "Canadian Grand Prix", "circuitCountry": "Canada", "circuitCity": "Mont-Tremblant" },
    {"circuitName": "Circuit of the Americas" , "circuitLength": 5.513, "circuitTurns": 20, "circuitGrandPrix": "United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Austin" },
    {"circuitName": "Circuit Paul Ricard" , "circuitLength": 5.842, "circuitTurns": 15, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Le Castellet" },
    {"circuitName": "Circuit Zandvoort" , "circuitLength": 4.259, "circuitTurns": 14, "circuitGrandPrix": "Dutch Grand Prix", "circuitCountry": "Netherlands", "circuitCity": "Zandvoort" },
    {"circuitName": "Circuit Zolder" , "circuitLength": 4.262, "circuitTurns": 10, "circuitGrandPrix": "Belgian Grand Prix", "circuitCountry": "Belgium", "circuitCity": "Heusden-Zolder" },
    {"circuitName": "Circuito da Boavista" , "circuitLength": 7.775, "circuitTurns": 15, "circuitGrandPrix": "Portuguese Grand Prix", "circuitCountry": "Portugal", "circuitCity": "Porto" },
    {"circuitName": "Circuito de Monsanto" , "circuitLength": 5.440, "circuitTurns": 9, "circuitGrandPrix": "Portuguese Grand Prix", "circuitCountry": "Portugal", "circuitCity": "Lisbon" },
    {"circuitName": "Circuito Permanente de Jerez" , "circuitLength": 4.428, "circuitTurns": 13, "circuitGrandPrix": "Spanish Grand Prix,European Grand Prix", "circuitCountry": "Spain", "circuitCity": "Jerez de la Frontera" },
    {"circuitName": "Circuito Permanente del Jarama" , "circuitLength": 3.314, "circuitTurns": 12, "circuitGrandPrix": "Spanish Grand Prix", "circuitCountry": "Spain", "circuitCity": "San Sebastián de los Reyes" },
    {"circuitName": "Dallas Fair Park" , "circuitLength": 3.901, "circuitTurns": 14, "circuitGrandPrix": "Dallas Grand Prix", "circuitCountry": "United States", "circuitCity": "Dallas" },
    {"circuitName": "Detroit Street Circuit" , "circuitLength": 4.023, "circuitTurns": 20, "circuitGrandPrix": "Detroit Grand Prix", "circuitCountry": "United States", "circuitCity": "Detroit" },
    {"circuitName": "Donington Park" , "circuitLength": 4.020, "circuitTurns": 11, "circuitGrandPrix": "European Grand Prix", "circuitCountry": "United Kingdom", "circuitCity": "Castle Donington" },
    {"circuitName": "Fuji Speedway" , "circuitLength": 4.563, "circuitTurns": 16, "circuitGrandPrix": "Japanese Grand Prix", "circuitCountry": "Japan", "circuitCity": "Oyama" },
    {"circuitName": "Hockenheimring" , "circuitLength": 4.574, "circuitTurns": 16, "circuitGrandPrix": "German Grand Prix", "circuitCountry": "Germany", "circuitCity": "Hockenheim" },
    {"circuitName": "Hungaroring" , "circuitLength": 4.381, "circuitTurns": 14, "circuitGrandPrix": "Hungarian Grand Prix", "circuitCountry": "Hungary", "circuitCity": "Mogyoród" },
    {"circuitName": "Indianapolis Motor Speedway" , "circuitLength": 4.192, "circuitTurns": 13, "circuitGrandPrix": "Indianapolis 500[d],United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Speedway" },
    {"circuitName": "Intercity Istanbul Park" , "circuitLength": 5.338, "circuitTurns": 14, "circuitGrandPrix": "Turkish Grand Prix", "circuitCountry": "Turkey", "circuitCity": "Istanbul" },
    {"circuitName": "Jeddah Corniche Circuit" , "circuitLength": 6.174, "circuitTurns": 27, "circuitGrandPrix": "Saudi Arabian Grand Prix", "circuitCountry": "Saudi Arabia", "circuitCity": "Jeddah" },
    {"circuitName": "Korea International Circuit" , "circuitLength": 5.615, "circuitTurns": 18, "circuitGrandPrix": "Korean Grand Prix", "circuitCountry": "South Korea", "circuitCity": "Yeongam" },
    {"circuitName": "Kyalami Grand Prix Circuit" , "circuitLength": 4.261, "circuitTurns": 13, "circuitGrandPrix": "South African Grand Prix", "circuitCountry": "South Africa", "circuitCity": "Midrand" },
    {"circuitName": "Las Vegas Strip Circuit" , "circuitLength": 6.201, "circuitTurns": 17, "circuitGrandPrix": "Las Vegas Grand Prix", "circuitCountry": "United States", "circuitCity": "Paradise" },
    {"circuitName": "Long Beach Street Circuit" , "circuitLength": 3.275, "circuitTurns": 18, "circuitGrandPrix": "United States Grand Prix West", "circuitCountry": "United States", "circuitCity": "Long Beach" },
    {"circuitName": "Lusail International Circuit" , "circuitLength": 5.419, "circuitTurns": 16, "circuitGrandPrix": "Qatar Grand Prix", "circuitCountry": "Qatar", "circuitCity": "Lusail" },
    {"circuitName": "Madring" , "circuitLength": 5.474, "circuitTurns": 22, "circuitGrandPrix": "Spanish Grand Prix", "circuitCountry": "Spain", "circuitCity": "Barajas" },
    {"circuitName": "Marina Bay Street Circuit" , "circuitLength": 4.940, "circuitTurns": 19, "circuitGrandPrix": "Singapore Grand Prix", "circuitCountry": "Singapore", "circuitCity": "Marina Bay" },
    {"circuitName": "Miami International Autodrome" , "circuitLength": 5.412, "circuitTurns": 19, "circuitGrandPrix": "Miami Grand Prix", "circuitCountry": "United States", "circuitCity": "Miami Gardens" },
    {"circuitName": "Montjuïc circuit" , "circuitLength": 3.791, "circuitTurns": 18, "circuitGrandPrix": "Spanish Grand Prix", "circuitCountry": "Spain", "circuitCity": "Barcelona" },
    {"circuitName": "Mosport International Raceway" , "circuitLength": 3.957, "circuitTurns": 10, "circuitGrandPrix": "Canadian Grand Prix", "circuitCountry": "Canada", "circuitCity": "Bowmanville" },
    {"circuitName": "Nivelles-Baulers" , "circuitLength": 3.724, "circuitTurns": 7, "circuitGrandPrix": "Belgian Grand Prix", "circuitCountry": "Belgium", "circuitCity": "Nivelles" },
    {"circuitName": "Nürburgring" , "circuitLength": 5.148, "circuitTurns": 15, "circuitGrandPrix": "German Grand Prix,European Grand Prix,Luxembourg Grand Prix,Eifel Grand Prix", "circuitCountry": "Germany", "circuitCity": "Nürburg" },
    {"circuitName": "Pescara Circuit" , "circuitLength": 25.800, "circuitTurns": 24, "circuitGrandPrix": "Pescara Grand Prix", "circuitCountry": "Italy", "circuitCity": "Pescara" },
    {"circuitName": "Phoenix Street Circuit" , "circuitLength": 3.720, "circuitTurns": 12, "circuitGrandPrix": "United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Phoenix" },
    {"circuitName": "Prince George Circuit" , "circuitLength": 3.920, "circuitTurns": 8, "circuitGrandPrix": "South African Grand Prix", "circuitCountry": "South Africa", "circuitCity": "East London" },
    {"circuitName": "Red Bull Ring" , "circuitLength": 4.318, "circuitTurns": 10, "circuitGrandPrix": "Austrian Grand Prix,Styrian Grand Prix", "circuitCountry": "Austria", "circuitCity": "Spielberg" },
    {"circuitName": "Riverside International Raceway" , "circuitLength": 5.271, "circuitTurns": 9, "circuitGrandPrix": "United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Moreno Valley" },
    {"circuitName": "Rouen-Les-Essarts" , "circuitLength": 6.542, "circuitTurns": 13, "circuitGrandPrix": "French Grand Prix", "circuitCountry": "France", "circuitCity": "Orival" },
    {"circuitName": "Scandinavian Raceway" , "circuitLength": 4.031, "circuitTurns": 8, "circuitGrandPrix": "Swedish Grand Prix", "circuitCountry": "Sweden", "circuitCity": "Anderstorp" },
    {"circuitName": "Sebring Raceway" , "circuitLength": 8.356, "circuitTurns": 12, "circuitGrandPrix": "United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Sebring" },
    {"circuitName": "Sepang International Circuit" , "circuitLength": 5.543, "circuitTurns": 15, "circuitGrandPrix": "Malaysian Grand Prix", "circuitCountry": "Malaysia", "circuitCity": "Sepang" },
    {"circuitName": "Shanghai International Circuit" , "circuitLength": 5.451, "circuitTurns": 16, "circuitGrandPrix": "Chinese Grand Prix", "circuitCountry": "China", "circuitCity": "Shanghai" },
    {"circuitName": "Silverstone Circuit" , "circuitLength": 5.891, "circuitTurns": 18, "circuitGrandPrix": "British Grand Prix,70th Anniversary Grand Prix", "circuitCountry": "United Kingdom", "circuitCity": "Silverstone" },
    {"circuitName": "Sochi Autodrom" , "circuitLength": 5.848, "circuitTurns": 15, "circuitGrandPrix": "Russian Grand Prix", "circuitCountry": "Russia", "circuitCity": "Sochi" },
    {"circuitName": "Suzuka International Racing Course" , "circuitLength": 5.807, "circuitTurns": 18, "circuitGrandPrix": "Japanese Grand Prix", "circuitCountry": "Japan", "circuitCity": "Suzuka" },
    {"circuitName": "TI Circuit Aida" , "circuitLength": 3.703, "circuitTurns": 11, "circuitGrandPrix": "Pacific Grand Prix", "circuitCountry": "Japan", "circuitCity": "Mimasaka" },
    {"circuitName": "Valencia Street Circuit" , "circuitLength": 5.419, "circuitTurns": 25, "circuitGrandPrix": "European Grand Prix", "circuitCountry": "Spain", "circuitCity": "Valencia" },
    {"circuitName": "Watkins Glen International" , "circuitLength": 5.430, "circuitTurns": 10, "circuitGrandPrix": "United States Grand Prix", "circuitCountry": "United States", "circuitCity": "Watkins Glen" },
    {"circuitName": "Yas Marina Circuit" , "circuitLength": 5.281, "circuitTurns": 15, "circuitGrandPrix": "Abu Dhabi Grand Prix", "circuitCountry": "United Arab Emirates", "circuitCity": "Abu Dhabi" },
    {"circuitName": "Zeltweg Airfield" , "circuitLength": 3.186, "circuitTurns": 4, "circuitGrandPrix": "Austrian Grand Prix", "circuitCountry": "Austria", "circuitCity": "Zeltweg" }
]

results_data = [
    #Australin GP
    {"driverID": 7 , "constructorID": 4 , "circuitID": 4, "placement": 1, "points": 25},
    {"driverID": 1 , "constructorID": 1 , "circuitID": 4, "placement": 2, "points": 18},
    {"driverID": 5 , "constructorID": 2 , "circuitID": 4, "placement": 3, "points": 15},
    {"driverID": 6 , "constructorID": 2 , "circuitID": 4, "placement": 4, "points": 12},
    {"driverID": 13 , "constructorID": 7 , "circuitID": 4, "placement": 5, "points": 10},
    {"driverID": 10 , "constructorID": 5 , "circuitID": 4, "placement": 6, "points": 8},
    {"driverID": 15 , "constructorID": 8 , "circuitID": 4, "placement": 7, "points": 6},
    {"driverID": 4 , "constructorID": 3 , "circuitID": 4, "placement": 8, "points": 4},
    {"driverID": 8 , "constructorID": 4 , "circuitID": 4, "placement": 9, "points": 2},
    {"driverID": 3 , "constructorID": 3 , "circuitID": 4, "placement": 10, "points": 1},
    {"driverID": 11 , "constructorID": 6 , "circuitID": 4, "placement": 11, "points": 0},
    {"driverID": 2 , "constructorID": 9 , "circuitID": 4, "placement": 12, "points": 0},
    {"driverID": 18 , "constructorID": 10 , "circuitID": 4, "placement": 13, "points": 0},
    {"driverID": 17 , "constructorID": 10 , "circuitID": 4, "placement": 14, "points": 0},
    {"driverID": 21 , "constructorID": 1 , "circuitID": 4, "placement": -1, "points": 0},
    {"driverID": 16 , "constructorID": 8 , "circuitID": 4, "placement": -1, "points": 0},
    {"driverID": 9 , "constructorID": 5 , "circuitID": 4, "placement": -1, "points": 0},
    {"driverID": 14 , "constructorID": 7 , "circuitID": 4, "placement": -1, "points": 0},
    {"driverID": 12 , "constructorID": 6 , "circuitID": 4, "placement": -1, "points": 0},
    {"driverID": 20 , "constructorID": 9 , "circuitID": 4, "placement": -1, "points": 0},

    #Miami GP
    {"driverID": 8 , "constructorID":  4, "circuitID": 56, "placement": 1, "points": 25},
    {"driverID": 7 , "constructorID":  4, "circuitID": 56, "placement": 2, "points": 18},
    {"driverID": 5, "constructorID":  2, "circuitID": 56, "placement": 3, "points": 15},
    {"driverID": 1, "constructorID":  1, "circuitID": 56, "placement": 4, "points": 12},
    {"driverID": 13, "constructorID":  7, "circuitID": 56, "placement": 5, "points": 10},
    {"driverID": 6, "constructorID":  2, "circuitID": 56, "placement": 6 , "points": 8},
    {"driverID": 4, "constructorID":  3, "circuitID": 56, "placement": 7, "points": 6},
    {"driverID": 3, "constructorID":  3, "circuitID": 56, "placement": 8, "points": 4},
    {"driverID": 14, "constructorID":  7, "circuitID": 56, "placement": 9, "points": 2},
    {"driverID": 2, "constructorID":  1, "circuitID": 56, "placement": 10, "points": 1},
    {"driverID": 20, "constructorID":  9, "circuitID": 56, "placement": 11, "points": 0},
    {"driverID": 18, "constructorID":  10, "circuitID": 56, "placement": 12, "points": 0},
    {"driverID": 11, "constructorID":  6, "circuitID": 56, "placement": 13, "points": 0},
    {"driverID": 15, "constructorID":  8, "circuitID": 56, "placement": 14, "points": 0},
    {"driverID": 9, "constructorID":  5, "circuitID": 56, "placement": 15, "points": 0},
    {"driverID": 10, "constructorID":  5, "circuitID": 56, "placement": 16, "points": 0},
    {"driverID": 21, "constructorID":  9, "circuitID": 56, "placement": -1, "points": 0},
    {"driverID": 16, "constructorID":  8, "circuitID": 56, "placement": -1, "points": 0},
    {"driverID": 17, "constructorID":  10, "circuitID": 56, "placement": -1, "points": 0},
    {"driverID": 12, "constructorID":  6, "circuitID": 56, "placement": -1, "points": 0},

    #Mexico GP, circuitId = 7
]

with app.app_context():
    db.drop_all()
    
    db.create_all()
    
    for circuit in circuit_data:
        circuit_object = Circuits(circuitName = circuit["circuitName"], circuitLength = circuit["circuitLength"], circuitTurns = circuit["circuitTurns"], circuitGrandPrix = circuit["circuitGrandPrix"], circuitCountry = circuit["circuitCountry"], circuitCity = circuit["circuitCity"])
        db.session.add(circuit_object)
        db.session.commit()
    for driver in drivers_data:
        driver_object = Drivers(firstName = driver["firstName"] , lastName = driver["lastName"], dateOfBirth=driver["dateOfBirth"], nation=driver["nation"], debutSeason=driver["debutSeason"])
        db.session.add(driver_object)
        db.session.commit()
    for constructor in teams_data:
        constructor_object = Constructors( teamName = constructor["teamName"], teamColor= constructor["teamColor"], foundedYear=constructor["foundedYear"], countryBase =constructor["baseCountry"])
        db.session.add(constructor_object)
        db.session.commit()


    for result in results_data:
        result_object = Results( driverID = result["driverID"], constructorID= result["constructorID"], circuitID=result["circuitID"], placement =result["placement"], points = result["points"])
        db.session.add(result_object)
        db.session.commit()
    