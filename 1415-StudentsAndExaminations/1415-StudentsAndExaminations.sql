-- Last updated: 14/10/2025, 20:04:47
# Write your MySQL query statement below
Select  S.student_id , S.student_name , J.subject_name , Count(E.subject_name) as attended_exams 
From Students S
cross join Subjects J 
left join Examinations E On S.student_id=E.student_id and E.subject_name =J.subject_name 
Group by S.student_id,S.student_name,J.subject_name
ORDER BY S.student_id, J.subject_name;