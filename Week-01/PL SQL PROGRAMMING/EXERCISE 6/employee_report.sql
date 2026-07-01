DELIMITER $$

CREATE PROCEDURE EmployeeSalaryReport()

BEGIN

    DECLARE done INT DEFAULT FALSE;

    DECLARE e_name VARCHAR(100);
    DECLARE e_salary DECIMAL(10,2);

    DECLARE cur CURSOR FOR

    SELECT
    Name,
    Salary

    FROM Employees;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND
    SET done = TRUE;

    OPEN cur;

    read_loop: LOOP

        FETCH cur
        INTO e_name,e_salary;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT
        e_name AS EmployeeName,
        e_salary AS Salary;

    END LOOP;

    CLOSE cur;

END $$

DELIMITER ;