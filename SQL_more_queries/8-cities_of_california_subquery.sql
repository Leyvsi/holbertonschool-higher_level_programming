-- Lists all cities of California from hbtn_0d_usa
-- Results are sorted by cities.id in ascending order
-- The use of JOIN is prohibited
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
