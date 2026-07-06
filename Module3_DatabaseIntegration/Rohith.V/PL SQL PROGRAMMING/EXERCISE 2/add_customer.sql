DELIMITER $$

CREATE PROCEDURE AddCustomer(
    IN cid INT,
    IN cname VARCHAR(100),
    IN dob DATE,
    IN bal DECIMAL(10,2)
)
BEGIN

    DECLARE custCount INT;

    SELECT COUNT(*)
    INTO custCount
    FROM Customers
    WHERE CustomerID = cid;

    IF custCount > 0 THEN

        SELECT 'Customer ID Already Exists'
        AS Message;

    ELSE

        INSERT INTO Customers
        VALUES(
            cid,
            cname,
            dob,
            bal,
            CURDATE(),
            NULL
        );

        SELECT 'Customer Added Successfully'
        AS Message;

    END IF;

END $$

DELIMITER ;