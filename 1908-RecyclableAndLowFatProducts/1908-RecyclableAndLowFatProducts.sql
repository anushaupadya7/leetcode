-- Last updated: 08/10/2025, 22:42:54
# Write your MySQL query statement below
Select P.product_id  
from Products P
where P.low_fats = 'Y' and P.recyclable = 'Y'