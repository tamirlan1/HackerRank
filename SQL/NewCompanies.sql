-- Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 

-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

-- Note:

-- The tables may contain duplicate records.
-- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

SELECT C.company_code, founder, num_lm, num_sm, num_m, num_e
FROM Company AS C
JOIN (SELECT company_code, count(distinct lead_manager_code) AS num_lm
     FROM Lead_Manager
     GROUP BY company_code) AS LM ON C.company_code = LM.company_code
JOIN (SELECT company_code, count(distinct senior_manager_code) AS num_sm
     FROM Senior_Manager
     GROUP BY company_code) AS SM ON C.company_code = SM.company_code
JOIN (SELECT company_code, count(distinct manager_code) AS num_m
     FROM Manager
     GROUP BY company_code) AS M ON C.company_code = M.company_code
JOIN (SELECT company_code, count(distinct employee_code) AS num_e
     FROM Employee
     GROUP BY company_code) AS E ON C.company_code = E.company_code
ORDER BY C.company_code