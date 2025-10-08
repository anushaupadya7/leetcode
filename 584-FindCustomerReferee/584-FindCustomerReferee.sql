-- Last updated: 08/10/2025, 22:51:09
# Write your MySQL query statement below
Select C.name
From Customer C
Where C.referee_id != 2 or C.referee_id IS NULL