-- You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table.

-- If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.

-- Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.

Select Start_Date, MIN(End_Date)
From
    (Select b.Start_Date
    From Projects as a
    RIGHT Join Projects as b
    ON b.Start_Date = a.End_Date
    WHERE a.Start_Date IS NULL
    ) sd,
    (Select a.End_Date
    From Projects as a
    Left Join Projects as b
    ON b.Start_Date = a.End_Date
    WHERE b.End_Date IS NULL
    ) ed
Where Start_Date < End_Date
GROUP BY Start_Date
ORDER BY datediff(MIN(End_Date), Start_Date), Start_Date