-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE total FLOAT DEFAULT 0;
    DECLARE counted FLOAT DEFAULT 0;

    SELECT SUM(score) INTO total
        FROM corrections
        WHERE corrections.user_id = user_id;

    SELECT COUNT(*) INTO counted
        FROM corrections
        WHERE corrections.user_id = user_id;

    UPDATE users 
        SET users.average_score = IF(counted = 0, 0, total / counted)
        WHERE users.id = user_id;
END;
|
