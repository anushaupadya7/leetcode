-- Last updated: 10/10/2025, 00:55:31
# Write your MySQL query statement below
Select W1.id
From Weather W1
join Weather W2 ON W1.recordDate = DATE_ADD(W2.recordDate,INTERVAL 1 DAY)
where W1.temperature > W2.temperature
