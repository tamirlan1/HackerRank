-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

SELECT S.hacker_id, name
FROM SUBMISSIONS AS S
JOIN HACKERS AS H ON S.hacker_id = H.hacker_id
JOIN Challenges AS C ON S.challenge_id = C.challenge_id
JOIN Difficulty AS D ON C.difficulty_level = D.difficulty_level
WHERE S.score = D.score
GROUP BY name, S.hacker_id
HAVING count(S.challenge_id) > 1
ORDER BY count(S.challenge_id) DESC, S.hacker_id