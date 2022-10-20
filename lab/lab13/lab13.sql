.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest ASC LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT f.pet, f.song, f.color, s.color FROM students f, students s
   WHERE f.pet = s.pet            
   AND f.song = s.song
   AND f.time < s.time; ;

CREATE TABLE smallest_int_having AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
