-- List all records of the table second_table where name is not empty
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
