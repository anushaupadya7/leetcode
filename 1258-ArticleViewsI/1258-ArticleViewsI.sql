-- Last updated: 08/10/2025, 23:11:36
# Write your MySQL query statement below
Select Distinct V.author_id as id
From Views V
Where V.author_id = V.viewer_id 
Order By id ASC
