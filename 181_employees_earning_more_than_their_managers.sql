# Write your MySQL query statement below
SELECT Name As Employee FROM Employee E1 WHERE Salary > (SELECT Salary FROM Employee E2 WHERE E2.Id=E1.ManagerId)
