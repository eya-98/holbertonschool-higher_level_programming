--  lists the number of records with the same score in the table 

SELECT score, count(*) as number FROM second_table GROUP BY score ORDER BY number DESC;