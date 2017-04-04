-- Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

SELECT * FROM (SELECT H.hacker_id, name, COUNT(*) AS NUM
FROM Hackers AS H
JOIN Challenges AS C ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, name
HAVING COUNT(*) = (SELECT MAX(M) FROM (SELECT COUNT(*) AS M FROM Challenges GROUP BY hacker_id) AS T)
ORDER BY H.hacker_id) AS T1
UNION
SELECT * FROM
(SELECT hacker_id, name, NUM FROM
(SELECT H.hacker_id, name, COUNT(*) AS NUM
FROM Hackers AS H
JOIN Challenges AS C ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, name) AS T7
JOIN 
(SELECT M FROM
(SELECT COUNT(*) AS M 
FROM Challenges 
GROUP BY hacker_id
) AS T4
GROUP BY M
HAVING COUNT(*) = 1) AS T5
ON M = NUM
ORDER BY NUM DESC
) AS SSS