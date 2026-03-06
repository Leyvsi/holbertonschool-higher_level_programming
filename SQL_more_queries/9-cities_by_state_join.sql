-- Lists all cities and their corresponding states
-- Results display: cities.name - states.name
SELECT cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
