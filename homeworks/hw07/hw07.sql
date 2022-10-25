CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size FROM dogs JOIN sizes WHERE dogs.height > sizes.min AND  dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child FROM parents JOIN dogs ON dogs.name = parents.parent ORDER BY dogs.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT DISTINCT 
  CASE WHEN p1.child > p2.child THEN p2.child ELSE p1.child END as sibling1,
  CASE WHEN p1.child < p2.child THEN p2.child ELSE p1.child END as sibling2
  FROM parents p1 JOIN parents p2 WHERE p1.parent = p2.parent AND p1.child != p2.child; 
-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT siblings.sibling1 || ' and ' || siblings.sibling2 || ' are ' || s1.size || ' siblings'
  FROM siblings
  JOIN size_of_dogs AS s1 ON siblings.sibling1 = s1.name
  JOIN size_of_dogs AS s2 ON siblings.sibling2 = s2.name
  WHERE s1.size = s2.size;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
