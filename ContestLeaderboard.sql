-- You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

-- The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

SELECT C.hacker_id, C.name, SUM(SC) AS TSC 
FROM Hackers AS C
JOIN
(SELECT hacker_id, challenge_id, MAX(score) AS SC
FROM Submissions
GROUP BY hacker_id, challenge_id
) AS T1
ON C.hacker_id = T1.hacker_id
GROUP BY C.hacker_id, C.name
HAVING TSC > 0
ORDER BY TSC DESC, C.hacker_id
