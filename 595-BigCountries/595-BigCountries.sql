-- Last updated: 08/10/2025, 23:05:55
# Write your MySQL query statement below
Select W.name,W.population,W.area
From World W
Where W.area >= 3000000 or W.population >= 25000000