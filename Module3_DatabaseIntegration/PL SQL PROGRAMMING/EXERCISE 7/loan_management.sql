DELIMITER $$

CREATE PROCEDURE GetLoanDetails(
    IN loanId INT
)

BEGIN

    SELECT *
    FROM Loans

    WHERE LoanID = loanId;

END $$

DELIMITER ;