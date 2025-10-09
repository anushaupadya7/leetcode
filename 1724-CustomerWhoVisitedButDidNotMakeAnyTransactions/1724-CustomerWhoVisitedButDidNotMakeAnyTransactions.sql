-- Last updated: 09/10/2025, 23:15:44
# Write your MySQL query statement below
Select V.customer_id,Count(V.customer_id) as count_no_trans 
From Visits V
Left Join Transactions T on V.visit_id = T.visit_id
Where T.visit_id is null
Group By V.customer_id