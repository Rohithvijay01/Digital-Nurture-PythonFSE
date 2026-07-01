DELIMITER $$

CREATE FUNCTION CalculateLoanInterest(
    loanAmount DECIMAL(10,2),
    interestRate DECIMAL(5,2)
)
RETURNS DECIMAL(10,2)

DETERMINISTIC

BEGIN

    RETURN
    (loanAmount * interestRate) / 100;

END $$

DELIMITER ;