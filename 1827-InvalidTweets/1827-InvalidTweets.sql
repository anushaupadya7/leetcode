-- Last updated: 08/10/2025, 23:41:45
# Write your MySQL query statement below
Select T.tweet_id
From Tweets T
Where Length(T.content) > 15