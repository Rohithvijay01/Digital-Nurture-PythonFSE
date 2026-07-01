DELIMITER $$

CREATE PROCEDURE GetEmployeeDetails(
    IN empId INT
)

BEGIN

    SELECT *
    FROM Employees

    WHERE EmployeeID = empId;

END $$

DELIMITER ;