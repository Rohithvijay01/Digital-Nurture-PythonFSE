CREATE TABLE TransactionAudit (

    AuditID INT AUTO_INCREMENT PRIMARY KEY,

    TransactionID INT,

    ActionDate DATETIME,

    ActionType VARCHAR(20)

);
DELIMITER $$

CREATE TRIGGER Transaction_Insert_Trigger

AFTER INSERT ON Transactions

FOR EACH ROW

BEGIN

    INSERT INTO TransactionAudit
    (
        TransactionID,
        ActionDate,
        ActionType
    )

    VALUES
    (
        NEW.TransactionID,
        NOW(),
        'INSERT'
    );

END $$

DELIMITER ;