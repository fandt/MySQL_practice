UPDATE company, 

(SELECT * FROM
(SELECT * , COUNT(is_key) - SUM(CASE WHEN is_key="no" THEN 1 ELSE 0 END) AS counts
FROM company
GROUP BY companyname
) AS yesno
WHERE counts = 0
) AS nono

SET company.is_key = 'yes'
WHERE nono.id = company.id
