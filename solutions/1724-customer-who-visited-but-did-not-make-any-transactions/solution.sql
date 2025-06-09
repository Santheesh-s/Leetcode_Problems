SELECT V.customer_id,COUNT(*) AS count_no_trans FROM Visits V WHERE V.visit_id NOT IN (SELECT visit_id FROM Transactions) GROUP BY V.customer_id;
