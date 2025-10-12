-- Last updated: 12/10/2025, 20:11:40
# Write your MySQL query statement below
SELECT E.name,B.bonus
FROM employee E
LEFT JOIN bonus B on E.empId=B.empid
WHERE B.bonus<1000 or B.bonus IS NULL
