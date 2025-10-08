-- Last updated: 08/10/2025, 23:41:53
# Write your MySQL query statement below
Select U.unique_id as unique_id  ,E.name
From Employees E
LEFT JOIN EmployeeUNI U ON E.id=U.id 