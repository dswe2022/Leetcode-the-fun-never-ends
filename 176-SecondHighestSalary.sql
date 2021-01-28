--  Leetcode 176. Second Highest Salary
--  Easy 1/28/21 

--  Write a SQL query to get the second highest salary from the Employee table.

--  +----+--------+
--  | Id | Salary |
--  +----+--------+
--  | 1  | 100    |
--  | 2  | 200    |
--  | 3  | 300    |
--  +----+--------+
--  For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

--  +---------------------+
--  | SecondHighestSalary |
--  +---------------------+
--  | 200                 |
--  +---------------------+

-- Approach: Using sub-query and LIMIT clause [Accepted]


SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;



-- Approach: Using IFNULL and LIMIT clause [Accepted]
-- Another way to solve the 'NULL' problem is to use IFNULL funtion as below.


SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary