CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d_child.name
    FROM parents AS p,dogs AS d_child,dogs AS d_parent
    WHERE p.child = d_child.name AND p.parent = d_parent.name
    ORDER BY d_parent.height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size
    FROM dogs AS d, sizes AS s
    WHERE s.min < d.height AND s.max >= d.height;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT d1.name AS siblings1, d2.name AS siblings2, s.size
    FROM parents AS p1, parents AS p2, dogs AS d1, dogs AS d2,sizes AS s
    WHERE p1.parent = p2.parent 
      AND p1.child = d1.name AND p2.child = d2.name 
      AND d1.height > s.min AND d1.height <= s.max
      AND d2.height > s.min AND d2.height <= s.max
      AND d1.name < d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || siblings1 || ' and ' || siblings2 || ', have the same size: ' || size AS sentence
    FROM siblings;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, MAX(height) - MIN(height) AS height_range
  FROM dogs
  GROUP BY fur
  HAVING MIN(height) >= (AVG(height) * 0.7) and MAX(height) <= (AVG(height) * 1.3) ;

