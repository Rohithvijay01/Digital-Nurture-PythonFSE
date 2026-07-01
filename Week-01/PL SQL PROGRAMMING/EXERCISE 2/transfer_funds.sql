DELIMITER $$

CREATE PROCEDURE TransferFunds(
    IN fromAcc INT,
    IN toAcc INT,
    IN amt DECIMAL(10,2)
)
BEGIN

    DECLARE fromBalance DECIMAL(10,2);

    SELECT Balance
    INTO fromBalance
    FROM Accounts
    WHERE AccountID = fromAcc;

    IF fromBalance < amt THEN

        SELECT 'Insufficient Balance' AS Message;

    ELSE

        UPDATE Accounts
        SET Balance = Balance - amt
        WHERE AccountID = fromAcc;

        UPDATE Accounts
        SET Balance = Balance + amt
        WHERE AccountID = toAcc;

        SELECT 'Transfer Successful' AS Message;

    END IF;

END $$

DELIMITER ;