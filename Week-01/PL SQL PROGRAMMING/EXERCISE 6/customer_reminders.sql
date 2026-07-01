DELIMITER $$

CREATE PROCEDURE CustomerBalanceReport()

BEGIN

    DECLARE done INT DEFAULT FALSE;
    DECLARE c_name VARCHAR(100);
    DECLARE c_balance DECIMAL(10,2);

    DECLARE cur CURSOR FOR
        SELECT Name, Balance
        FROM Customers;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND
    SET done = TRUE;

    OPEN cur;

    read_loop: LOOP

        FETCH cur
        INTO c_name, c_balance;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT
        c_name AS CustomerName,
        c_balance AS Balance;

    END LOOP;

    CLOSE cur;

END $$

DELIMITER ;