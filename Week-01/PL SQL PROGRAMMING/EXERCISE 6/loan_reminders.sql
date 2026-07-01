DELIMITER $$

CREATE PROCEDURE LoanReminder()

BEGIN

    DECLARE done INT DEFAULT FALSE;

    DECLARE l_id INT;
    DECLARE c_id INT;
    DECLARE e_date DATE;

    DECLARE cur CURSOR FOR

    SELECT
    LoanID,
    CustomerID,
    EndDate

    FROM Loans

    WHERE EndDate <=
    DATE_ADD(CURDATE(),INTERVAL 30 DAY);

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND
    SET done = TRUE;

    OPEN cur;

    read_loop: LOOP

        FETCH cur
        INTO l_id,c_id,e_date;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT
        l_id AS LoanID,
        c_id AS CustomerID,
        e_date AS DueDate;

    END LOOP;

    CLOSE cur;

END $$

DELIMITER ;