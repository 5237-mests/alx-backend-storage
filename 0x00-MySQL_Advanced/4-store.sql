-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS decreased;

DELIMITER |
CREATE TRIGGER decreased AFTER INSERT ON orders
    FOR EACH ROW
    BEGIN
        UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
    END;
|
