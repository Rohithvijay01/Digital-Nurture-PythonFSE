DELIMITER $$

CREATE FUNCTION AccountStatus(
    bal DECIMAL(10,2)
)
RETURNS VARCHAR(20)

DETERMINISTIC

BEGIN

    IF bal >= 10000 THEN
        RETURN 'Premium';
    ELSE
        RETURN 'Regular';
    END IF;

END $$

DELIMITER ;