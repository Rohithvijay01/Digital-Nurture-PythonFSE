DELIMITER $$

CREATE TRIGGER Loan_Validation_Trigger

BEFORE INSERT ON Loans

FOR EACH ROW

BEGIN

    IF NEW.LoanAmount < 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT =
        'Loan Amount Cannot Be Negative';

    END IF;

END $$

DELIMITER ;