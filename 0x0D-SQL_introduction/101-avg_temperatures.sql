-- displays the average temperature

SELECT city, AVG(value) as tem FROM temperatures GROUP BY city ORDER BY tem DESC;