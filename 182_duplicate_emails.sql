# Write your MySQL query statement below
# SELECT Email FROM (SELECT Email, COUNT(Email) AS EmailCount FROM Person GROUP BY Email) AS Email WHERE EmailCount > 1;
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;