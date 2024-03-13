-- Displays the top 3 cities with the highest average temperature between July and August ordered by temperature(descending).
SELECT 'city', AVG('value') AS 'avg_temp'
FROM 'temperature'
WHERE 'mont' = 7 OR 'month' = 8
GROUP BY 'city'
ORDER BY 'avg_temp' DESC
LIMIT 3;

