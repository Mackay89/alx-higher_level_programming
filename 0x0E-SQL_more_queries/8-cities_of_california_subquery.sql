-- task: Script to list all cities of California in the database hbtn_0d_usa.
-- lists all rows of a column in a database
SELLECT id,, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
