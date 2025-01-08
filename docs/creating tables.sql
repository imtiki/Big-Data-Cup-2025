CREATE TABLE ba_tracking(
"Image Id" VARCHAR(100),
"Period" INT,
"Game Clock" VARCHAR(100),
"Player or Puck" VARCHAR(100),
"Team" VARCHAR(100),
"Player Id" INT,
"Rink Location X (Feet)" DECIMAL, 
"Rink Location Y (Feet)" DECIMAL,
"Rink Location Z (Feet)" DECIMAL,
"Goal Score" VARCHAR(100)
);
CREATE TABLE dc_tracking(
"Image Id" VARCHAR(100),
"Period" INT,
"Game Clock" VARCHAR(100),
"Player or Puck" VARCHAR(100),
"Team" VARCHAR(100),
"Player Id" INT,
"Rink Location X (Feet)" DECIMAL, 
"Rink Location Y (Feet)" DECIMAL,
"Rink Location Z (Feet)" DECIMAL,
"Goal Score" VARCHAR(100)
);
CREATE TABLE fe_tracking(
"Image Id" VARCHAR(100),
"Period" INT,
"Game Clock" VARCHAR(100),
"Player or Puck" VARCHAR(100),
"Team" VARCHAR(100),
"Player Id" INT,
"Rink Location X (Feet)" DECIMAL, 
"Rink Location Y (Feet)" DECIMAL,
"Rink Location Z (Feet)" DECIMAL,
"Goal Score" VARCHAR(100)
);
CREATE TABLE ba_shifts(
"Date" VARCHAR(100),
"Game Name" VARCHAR(100),
"Team Name" VARCHAR(100),
"Player Id" VARCHAR(100),
"Shift Number" INT,
"Period" INT,
"Start Clock" VARCHAR(100),
"End Clock" VARCHAR(100),
"Shift Length" VARCHAR(100)
)
CREATE TABLE ba_events(
"Date" VARCHAR(100),
"Home Team" VARCHAR(100),
"Away Team" VARCHAR(100),
"Period" INT,
"Clock" VARCHAR(100),
"Home Team Skaters" INT,
"Away Team Skaters" INT,
"Home Team Goals" INT,
"Away Team Goals" INT,
"Team" VARCHAR(100),
"Player Id" INT,
"Event" VARCHAR(100),
"X Coordinate" INT,
"Y Coordinate" DECIMAL,
"Detail 1" VARCHAR(100),
"Detail 2" VARCHAR(100),
"Detail 3" DECIMAL,
"Detail 4" VARCHAR(100),
"Player Id 2" DECIMAL,
"X Coordinate 2" DECIMAL,
"Y Coordinate 2" DECIMAL
)