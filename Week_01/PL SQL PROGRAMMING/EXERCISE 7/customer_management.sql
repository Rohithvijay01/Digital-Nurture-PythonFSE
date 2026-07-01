DELIMITER $$

CREATE PROCEDURE GetCustomerBalance(
    IN custId INT
)

BEGIN

    SELECT
    CustomerID,
    Name,
    Balance

    FROM Customers

    WHERE CustomerID = custId;

END $$

DELIMITER ;