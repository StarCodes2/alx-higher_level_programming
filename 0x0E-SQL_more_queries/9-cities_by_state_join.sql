-- Prints all cities contained in the databet
SELECT cities_id, cities.name, states.name
from cities
LEFT JOIN states
oN state_id = states.id
ORDER BY cities.id ASC;
