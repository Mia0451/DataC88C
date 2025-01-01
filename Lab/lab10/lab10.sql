CREATE TABLE turkeys AS
  SELECT 18 AS age, 16.5 AS weight, "Pecan" AS name UNION
  SELECT 30       , 22.1          , "Waddle"        UNION
  SELECT 12       , 17.3          , "Bud"           UNION
  SELECT 14       , 15.3          , "Bird"          UNION
  SELECT 30       , 26.8          , "Tom"           UNION
  SELECT 26       , 18.4          , "Flappy"        UNION
  SELECT 18       , 19.3          , "Pumpkin";

CREATE TABLE big AS
  SELECT name, weight * 2.2 AS pounds
  FROM turkeys
  WHERE weight > 18
  ORDER by name;

CREATE TABLE growing AS
  SELECT name, MAX(weight, weight + (24 - age)) AS full
  From turkeys
  WHERE full > 25;

