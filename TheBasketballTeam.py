import sqlite3
from random import randint

conn = sqlite3.connect("TheBasketballTeam.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")
sql = ""
values = []
value = ()

#Strings to create each table
createPlayersTableQuery = """CREATE TABLE IF NOT EXISTS [players] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255),
  [jersey_number] integer
  )"""

createCoachesTableQuery = """CREATE TABLE IF NOT EXISTS [coaches] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
  )"""

createTeamTableQuery = """CREATE TABLE IF NOT EXISTS [team] (
  [id] integer PRIMARY KEY,
  [team_name] nvarchar(255),
  [city_id] integer,
  FOREIGN KEY(city_id) REFERENCES city(id)
  )"""

createCityTableQuery = """CREATE TABLE IF NOT EXISTS [city] (
  [id] integer PRIMARY KEY,
  [city_name] nvarchar(255)
  )"""

createTeamAssignmentTableQuery = """CREATE TABLE IF NOT EXISTS [team_assignment] (
  [team_id] integer,
  [player1_id] integer,
  [player2_id] integer,
  [player3_id] integer,
  [player4_id] integer,
  [player5_id] integer,
  [player6_id] integer,
  [player7_id] integer,
  [player8_id] integer,
  [player9_id] integer,
  [player10_id] integer,
  [player11_id] integer,
  [player12_id] integer,
  [coach1_id] integer,
  [coach2_id] integer,
  [coach3_id] integer,
  FOREIGN KEY(team_id) REFERENCES team(id),
  FOREIGN KEY(player1_id) REFERENCES players(id),
  FOREIGN KEY(player2_id) REFERENCES players(id),
  FOREIGN KEY(player3_id) REFERENCES players(id),
  FOREIGN KEY(player4_id) REFERENCES players(id),
  FOREIGN KEY(player5_id) REFERENCES players(id),
  FOREIGN KEY(player6_id) REFERENCES players(id),
  FOREIGN KEY(player7_id) REFERENCES players(id),
  FOREIGN KEY(player8_id) REFERENCES players(id),
  FOREIGN KEY(player9_id) REFERENCES players(id),
  FOREIGN KEY(player10_id) REFERENCES players(id),
  FOREIGN KEY(player11_id) REFERENCES players(id),
  FOREIGN KEY(player12_id) REFERENCES players(id),
  FOREIGN KEY(coach1_id) REFERENCES coaches(id),
  FOREIGN KEY(coach2_id) REFERENCES coaches(id),
  FOREIGN KEY(coach3_id) REFERENCES coaches(id)
  )"""
  
createGamesTableQuery = """CREATE TABLE IF NOT EXISTS [games] (
  [home_team] nvarchar(255),
  [home_score] int,
  [visitor_team] nvarchar(255),
  [visitor_score] int,
  [date_game] date,
  FOREIGN KEY(home_team) REFERENCES team(id),
  FOREIGN KEY(visitor_team) REFERENCES team(id)
  )"""

#Create Tables
cursor.execute(createPlayersTableQuery)
cursor.execute(createCoachesTableQuery)
cursor.execute(createTeamTableQuery)
cursor.execute(createCityTableQuery)
cursor.execute(createTeamAssignmentTableQuery)
cursor.execute(createGamesTableQuery)

#Insert Sample Data to Players Table
sql = "INSERT INTO players (last_name, first_name, middle_name, jersey_number) \
  values (:values(0), :values(1), :values(2), :values(3))"
values = [
  ("James", "Butt", "Orleans",randint(1, 99)),
  ("Josephine", "Darakjy", "Livingston",randint(1, 99)),
  ("Art", "Venere", "Gloucester",randint(1, 99)),
  ("Lenna", "Paprocki", "Anchorage",randint(1, 99)),
  ("Donette", "Foller", "Butler",randint(1, 99)),
  ("Simona", "Morasca", "Ashland",randint(1, 99)),
  ("Mitsue", "Tollner", "Cook",randint(1, 99)),
  ("Leota", "Dilliard", "Santa Clara",randint(1, 99)),
  ("Sage", "Wieser", "Minnehaha",randint(1, 99)),
  ("Kris", "Marrier", "Baltimore City",randint(1, 99)),
  ("Minna", "Amigon", "Montgomery",randint(1, 99)),
  ("Abel", "Maclead", "Suffolk",randint(1, 99)),
  ("Kiley", "Caldarera", "Los Angeles",randint(1, 99)),
  ("Graciela", "Ruta", "Geauga",randint(1, 99)),
  ("Cammy", "Albares", "Webb",randint(1, 99)),
  ("Mattie", "Poquette", "Maricopa",randint(1, 99)),
  ("Meaghan", "Garufi", "Warren",randint(1, 99)),
  ("Gladys", "Rim", "Milwaukee",randint(1, 99)),
  ("Yuki", "Whobrey", "Wayne",randint(1, 99)),
  ("Fletcher", "Flosi", "Winnebago",randint(1, 99)),
  ("Bette", "Nicka", "Delaware",randint(1, 99)),
  ("Veronika", "Inouye", "Santa Clara",randint(1, 99)),
  ("Willard", "Kolmetz", "Dallas",randint(1, 99)),
  ("Maryann", "Royster", "Albany",randint(1, 99)),
  ("Alisha", "Slusarski", "Middlesex",randint(1, 99)),
  ("Allene", "Iturbide", "Portage",randint(1, 99)),
  ("Chanel", "Caudy", "Johnson",randint(1, 99)),
  ("Ezekiel", "Chui", "Talbot",randint(1, 99)),
  ("Willow", "Kusko", "New York",randint(1, 99)),
  ("Bernardo", "Figeroa", "Montgomery",randint(1, 99)),
  ("Ammie", "Corrio", "Franklin",randint(1, 99)),
  ("Francine", "Vocelka", "Dona Ana",randint(1, 99)),
  ("Ernie", "Stenseth", "Bergen",randint(1, 99)),
  ("Albina", "Glick", "Middlesex",randint(1, 99)),
  ("Alishia", "Sergi", "New York",randint(1, 99)),
  ("Solange", "Shinko", "Jefferson",randint(1, 99)),
  ("Jose", "Stockham", "New York",randint(1, 99)),
  ("Rozella", "Ostrosky", "Ventura",randint(1, 99)),
  ("Valentine", "Gillian", "Bexar",randint(1, 99)),
  ("Kati", "Rulapaugh", "Dickinson",randint(1, 99)),
  ("Youlanda", "Schemmer", "Crook",randint(1, 99)),
  ("Dyan", "Oldroyd", "Johnson",randint(1, 99)),
  ("Roxane", "Campain", "Fairbanks North Star",randint(1, 99)),
  ("Lavera", "Perin", "Miami-Dade",randint(1, 99)),
  ("Erick", "Ferencz", "Fairbanks North Star",randint(1, 99)),
  ("Fatima", "Saylors", "Hennepin",randint(1, 99)),
  ("Jina", "Briddick", "Suffolk",randint(1, 99)),
  ("Kanisha", "Waycott", "Los Angeles",randint(1, 99)),
  ("Emerson", "Bowley", "Dane",randint(1, 99)),
  ("Blair", "Malet", "Philadelphia",randint(1, 99)),
  ("Brock", "Bolognia", "New York",randint(1, 99)),
  ("Lorrie", "Nestle", "Coffee",randint(1, 99)),
  ("Sabra", "Uyetake", "Richland",randint(1, 99)),
  ("Marjory", "Mastella", "Delaware",randint(1, 99)),
  ("Karl", "Klonowski", "Hunterdon",randint(1, 99)),
  ("Tonette", "Wenner", "Nassau",randint(1, 99)),
  ("Amber", "Monarrez", "Montgomery",randint(1, 99)),
  ("Shenika", "Seewald", "Los Angeles",randint(1, 99)),
  ("Delmy", "Ahle", "Providence",randint(1, 99)),
  ("Deeanna", "Juhas", "Montgomery",randint(1, 99)),
  ("Blondell", "Pugh", "Providence",randint(1, 99)),
  ("Jamal", "Vanausdal", "Middlesex",randint(1, 99)),
  ("Cecily", "Hollack", "Travis",randint(1, 99)),
  ("Carmelina", "Lindall", "Douglas",randint(1, 99)),
  ("Maurine", "Yglesias", "Milwaukee",randint(1, 99)),
  ("Tawna", "Buvens", "New York",randint(1, 99)),
  ("Penney", "Weight", "Anchorage",randint(1, 99)),
  ("Elly", "Morocco", "Erie",randint(1, 99)),
  ("Ilene", "Eroman", "Anne Arundel",randint(1, 99)),
  ("Vallie", "Mondella", "Ada",randint(1, 99)),
  ("Kallie", "Blackwood", "San Francisco",randint(1, 99)),
  ("Johnetta", "Abdallah", "Orange",randint(1, 99)),
  ("Bobbye", "Rhym", "San Mateo",randint(1, 99)),
  ("Micaela", "Rhymes", "Contra Costa",randint(1, 99)),
  ("Tamar", "Hoogland", "Madison",randint(1, 99)),
  ("Moon", "Parlato", "Allegany",randint(1, 99)),
  ("Laurel", "Reitler", "Baltimore",randint(1, 99)),
  ("Delisa", "Crupi", "Essex",randint(1, 99)),
  ("Viva", "Toelkes", "Cook",randint(1, 99)),
  ("Elza", "Lipke", "Essex",randint(1, 99)),
  ("Devorah", "Chickering", "Curry",randint(1, 99)),
  ("Timothy", "Mulqueen", "Richmond",randint(1, 99)),
  ("Arlette", "Honeywell", "Duval",randint(1, 99)),
  ("Dominque", "Dickerson", "Alameda",randint(1, 99)),
  ("Lettie", "Isenhower", "Cuyahoga",randint(1, 99)),
  ("Myra", "Munns", "Tarrant",randint(1, 99)),
  ("Stephaine", "Barfield", "Los Angeles",randint(1, 99)),
  ("Lai", "Gato", "Cook",randint(1, 99)),
  ("Stephen", "Emigh", "Summit",randint(1, 99)),
  ("Tyra", "Shields", "Philadelphia",randint(1, 99)),
  ("Tammara", "Wardrip", "San Mateo",randint(1, 99)),
  ("Cory", "Gibes", "Los Angeles",randint(1, 99)),
  ("Danica", "Bruschke", "McLennan",randint(1, 99)),
  ("Wilda", "Giguere", "Anchorage",randint(1, 99)),
  ("Elvera", "Benimadho", "Santa Clara",randint(1, 99)),
  ("Carma", "Vanheusen", "Alameda",randint(1, 99)),
  ("Malinda", "Hochard", "Marion",randint(1, 99)),
  ("Natalie", "Fern", "Sweetwater",randint(1, 99)),
  ("Lisha", "Centini", "Fairfax",randint(1, 99)),
  ("Arlene", "Klusman", "Orleans",randint(1, 99))
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Players Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Coaches Table
sql = "INSERT INTO coaches (last_name, first_name, middle_name) \
  values (:values(0), :values(1), :values(2))"
values = [
  ("Cassi", "Wildfong", "Cook"),
  ("Britt", "Galam", "Montgomery"),
  ("Adell", "Lipkin", "Morris"),
  ("Jacqueline", "Rowling", "Erie"),
  ("Lonny", "Weglarz", "Salt Lake"),
  ("Lonna", "Diestel", "Cumberland"),
  ("Cristal", "Samara", "Los Angeles"),
  ("Kenneth", "Grenet", "Ingham"),
  ("Elli", "Mclaird", "Oneida"),
  ("Alline", "Jeanty", "St Joseph"),
  ("Sharika", "Eanes", "Orange"),
  ("Nu", "Mcnease", "Hudson"),
  ("Daniela", "Comnick", "Mercer"),
  ("Cecilia", "Colaizzo", "Dane"),
  ("Leslie", "Threets", "Westchester"),
  ("Nan", "Koppinger", "Guilford"),
  ("Izetta", "Dewar", "Baltimore City"),
  ("Tegan", "Arceo", "Middlesex"),
  ("Ruthann", "Keener", "Kerr"),
  ("Joni", "Breland", "Cook"),
  ("Vi", "Rentfro", "Monmouth"),
  ("Colette", "Kardas", "Douglas"),
  ("Malcolm", "Tromblay", "Fairfax"),
  ("Ryan", "Harnos", "Collin"),
  ("Jess", "Chaffins", "New York"),
  ("Sharen", "Bourbon", "Nassau"),
  ("Nickolas", "Juvera", "Citrus"),
  ("Gary", "Nunlee", "Hancock"),
  ("Diane", "Devreese", "Buchanan"),
  ("Roslyn", "Chavous", "Hinds"),
  ("Glory", "Schieler", "Taylor"),
  ("Rasheeda", "Sayaphon", "Santa Clara"),
  ("Alpha", "Palaia", "Camden"),
  ("Refugia", "Jacobos", "Alameda"),
  ("Shawnda", "Yori", "Seminole"),
  ("Mona", "Delasancha", "Laramie"),
  ("Gilma", "Liukko", "Nassau"),
  ("Janey", "Gabisi", "Dane"),
  ("Lili", "Paskin", "Hudson"),
  ("Loren", "Asar", "Lackawanna"),
  ("Dorothy", "Chesterfield", "San Diego"),
  ("Gail", "Similton", "Riverside"),
  ("Catalina", "Tillotson", "Atlantic"),
  ("Lawrence", "Lorens", "Providence"),
  ("Carlee", "Boulter", "Dickinson"),
  ("Thaddeus", "Ankeny", "Placer"),
  ("Jovita", "Oles", "Volusia"),
  ("Alesia", "Hixenbaugh", "District of Columbia"),
  ("Lai", "Harabedian", "Marin"),
  ("Brittni", "Gillaspie", "Ada"),
  ("Raylene", "Kampa", "Elkhart"),
  ("Flo", "Bookamer", "Box Butte"),
  ("Jani", "Biddy", "King"),
  ("Chauncey", "Motley", "Orange")
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Coaches Table: {cursor.rowcount} records inserted")

#Insert Sample Data to City Table
sql = "INSERT INTO city (city_name) \
  values (:values(0))"
values = [
  ("New York",),
  ("California",),
  ("Batangas",),
  ("Bacoor",),
  ("Cebu",),
  ("Baguio",)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"City Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Team Table
sql = "INSERT INTO team (team_name,city_id) \
  values (:values(0), :values(1))"
values = [
  ("Number Crunchers", 1),
  ("The Defenders", 2),
  ("Graph Masters", 3),
  ("Aaa Analytics", 4),
  ("Stock Holderz", 5),
  ("Data Commanders", 6)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Team Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Team Assignment Table
sql = """INSERT INTO team_assignment \
  values (:values(0), :values(1), :values(2), :values(3), :values(4),
  :values(5), :values(6), :values(7), :values(8), :values(9), :values(10),
  :values(11), :values(12), :values(13), :values(14), :values(15))
  """
values = [
  (1,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3),
  (2,13,14,15,16,17,18,19,20,21,22,23,24,4,5,6),
  (3,25,26,27,28,29,30,31,32,33,34,35,36,7,8,9),
  (4,37,38,39,40,41,42,43,44,45,46,47,48,10,11,12),
  (5,49,50,51,52,53,54,55,56,57,58,59,60,13,14,15),
  (6,61,62,63,64,65,66,67,68,69,70,71,72,16,17,18)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Team Assignment Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Games Table
sql = "INSERT INTO games \
  values (:values(0), :values(1), :values(2), :values(3), :values(4))"
values = [
  (1,80,2,81,"2023-10-28"),
  (3,67,4,45,"2023-10-29"),
  (5,72,6,91,"2023-10-30")
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Games Table: {cursor.rowcount} records inserted")

#close the cursor and connection
cursor.close
conn.close