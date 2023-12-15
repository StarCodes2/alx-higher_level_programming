-- Prints all cities contained in the databet
SELECT cities_id, cities.name, states.name
FROM cities
LEFT JOIN states
ON state_id = states.id
ORDER BY cities.id ASC;
