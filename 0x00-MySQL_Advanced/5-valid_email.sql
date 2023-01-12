-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed
DROP TRIGGER IF EXISTS validator;
DELIMITER |
CREATE TRIGGER validator BEFORE UPDATE  ON users
    FOR EACH ROW
    BEGIN
        -- UPDATE users SET valid_email = 0 WHERE email != NEW.email;
        IF OLD.email != NEW.email  THEN
            SET NEW.valid_email = 0;
        ELSE
            SET NEW.valid_email = NEW.valid_email;
        END IF;
    END;
|
