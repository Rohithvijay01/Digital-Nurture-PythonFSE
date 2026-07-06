DELIMITER $$

CREATE TRIGGER Customer_Update_Trigger

BEFORE UPDATE ON Customers

FOR EACH ROW

BEGIN

    SET NEW.LastModified = CURDATE();

END $$

DELIMITER ;