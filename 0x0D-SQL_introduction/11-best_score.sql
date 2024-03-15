-- task: Lists all records in the table secod_table with a score >= in my  MySQL server.
-- Records are ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
