DELIMITER $$

CREATE PROCEDURE TransferFundsSP(
    IN fromAccount INT,
    IN toAccount INT,
    IN amount DECIMAL(10,2)
)
BEGIN

    UPDATE Accounts
    SET Balance = Balance - amount
    WHERE AccountID = fromAccount;

    UPDATE Accounts
    SET Balance = Balance + amount
    WHERE AccountID = toAccount;

    SELECT 'Fund Transfer Successful'
    AS Message;

END $$

DELIMITER ;