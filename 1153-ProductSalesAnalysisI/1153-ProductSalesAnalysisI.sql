-- Last updated: 09/10/2025, 23:15:53
# Write your MySQL query statement below
Select P.product_name , S.year, S.price
From Sales S
INNER JOIN Product P ON S.product_id = P.product_id