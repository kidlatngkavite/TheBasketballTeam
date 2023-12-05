CREATE TABLE [players] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
)
GO

CREATE TABLE [coaches] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
)
GO

CREATE TABLE [team] (
  [id] integer PRIMARY KEY,
  [team_name] nvarchar(255),
  [city_id] integer
)
GO

CREATE TABLE [city] (
  [id] integer PRIMARY KEY,
  [city_name] nvarchar(255)
)
GO

CREATE TABLE [team_assignment] (
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
  [coach3_id] integer
)
GO

CREATE TABLE [games] (
  [home_team] nvarchar(255),
  [home_score] int,
  [visitor_team] nvarchar(255),
  [visitor_score] int,
  [date_game] date
)
GO

ALTER TABLE [team] ADD FOREIGN KEY ([city_id]) REFERENCES [city] ([id])
GO

ALTER TABLE [games] ADD FOREIGN KEY ([home_team]) REFERENCES [team] ([id])
GO

ALTER TABLE [games] ADD FOREIGN KEY ([visitor_team]) REFERENCES [team] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([team_id]) REFERENCES [team] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player1_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player2_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player3_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player4_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player5_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player6_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player7_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player8_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player9_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player10_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player11_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([player12_id]) REFERENCES [players] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([coach1_id]) REFERENCES [coaches] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([coach2_id]) REFERENCES [coaches] ([id])
GO

ALTER TABLE [team_assignment] ADD FOREIGN KEY ([coach3_id]) REFERENCES [coaches] ([id])
GO
