SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM Occupations
ORDER BY Name ASC;

SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', lower(Occupation), 's.')
FROM Occupations
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC, Occupation ASC;
