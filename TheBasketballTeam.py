import sqlite3

conn = sqlite3.connect("TheBasketballTeam.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")

createPlayersTableQuery = """CREATE TABLE IF NOT EXISTS [players] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
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

print(f"{createPlayersTableQuery}")
print(f"{createCoachesTableQuery}")
print(f"{createTeamTableQuery}")
print(f"{createCityTableQuery}")
print(f"{createTeamAssignmentTableQuery}")
print(f"{createGamesTableQuery}")


cursor.execute(createPlayersTableQuery)
cursor.execute(createCoachesTableQuery)
cursor.execute(createTeamTableQuery)
cursor.execute(createCityTableQuery)
cursor.execute(createTeamAssignmentTableQuery)
cursor.execute(createGamesTableQuery)
#conn.commit()