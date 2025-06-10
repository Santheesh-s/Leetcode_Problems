SELECT R.contest_id,ROUND(COUNT(R.user_id)/(SELECT COUNT(*) FROM Users)*100.0,2) AS percentage FROM Users U LEFT JOIN Register R ON U.user_id=R.user_id WHERE 
R.contest_id IS NOT NULL GROUP BY R.contest_id ORDER BY percentage desc,contest_id asc
