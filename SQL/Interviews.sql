-- Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are .

-- Note: A specific contest can be used to screen candidates at more than one college, but each college only holds screening contest.

SELECT CT.contest_id, CT.hacker_id, CT.name, SUM(TS), SUM(TAS), SUM(TV), SUM(TUV)
FROM Contests AS CT
JOIN Colleges AS CL ON CT.contest_id = CL.contest_id
JOIN Challenges AS CH ON CH.college_id = CL.college_id
left JOIN ( SELECT CHALLENGE_ID, SUM(total_views) AS TV, SUM(total_unique_views) AS TUV FROM View_Stats GROUP BY CHALLENGE_ID )  VS ON CH.challenge_id = VS.challenge_id
left JOIN (SELECT CHALLENGE_ID, SUM(TOTAL_SUBMISSIONS) AS TS, SUM(TOTAL_ACCEPTED_SUBMISSIONS) AS TAS FROM Submission_Stats GROUP BY CHALLENGE_ID ) AS SS ON CH.challenge_id = SS.challenge_id
GROUP BY CT.contest_id
ORDER BY CT.contest_id
