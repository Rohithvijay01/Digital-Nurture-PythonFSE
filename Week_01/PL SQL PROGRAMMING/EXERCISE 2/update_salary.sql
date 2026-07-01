DELIMITER $$

CREATE PROCEDURE UpdateSalary(
    IN empId INT,
    IN incrementAmt DECIMAL(10,2)
)
BEGIN

    DECLARE empCount INT;

    SELECT COUNT(*)
    INTO empCount
    FROM Employees
    WHERE EmployeeID = empId;

    IF empCount = 0 THEN

        SELECT 'Employee Not Found' AS Message;

    ELSE

        UPDATE Employees
        SET Salary = Salary + incrementAmt
        WHERE EmployeeID = empId;

        SELECT 'Salary Updated Successfully'
        AS Message;

    END IF;

END $$

DELIMITER ;