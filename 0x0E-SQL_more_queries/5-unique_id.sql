-- Creates a table called unique_id with a UNIQUE constraimt and a default
-- value of 1 added to the id field
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
