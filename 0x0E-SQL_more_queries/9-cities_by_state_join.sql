-- Prints all cities contained in the databet
SELECT cities_id, cities.name, state.name
from cities
LEFT JOIN stack
oN state_id = state.id
ODER BY cities.id ASC;
