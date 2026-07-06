SELECT c.Name,
       l.LoanID,
       l.EndDate
FROM Customers c
JOIN Loans l
ON c.CustomerID=l.CustomerID
WHERE l.EndDate
BETWEEN CURDATE()
AND DATE_ADD(CURDATE(),INTERVAL 30 DAY);